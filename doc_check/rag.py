"""RAG (Retrieval-Augmented Generation) functionality for document indexing and retrieval."""

import re
import hashlib
from pathlib import Path
from typing import List, Tuple, Optional
import pickle

import numpy as np
from sentence_transformers import SentenceTransformer
import faiss


class DocumentChunk:
    """Represents a chunk of document content with metadata."""
    
    def __init__(self, content: str, start_pos: int, end_pos: int, chunk_id: int):
        self.content = content
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.chunk_id = chunk_id


class RAGIndexer:
    """Handles document chunking, embedding, and retrieval for RAG."""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int = 512, chunk_overlap: int = 50):
        """Initialize the RAG indexer.
        
        Args:
            model_name: Name of the sentence transformer model to use for embeddings
            chunk_size: Size of each document chunk in characters
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.model_name = model_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_model = None
        self.index = None
        self.chunks = []
        
    def _load_embedding_model(self):
        """Lazy load the embedding model."""
        if self.embedding_model is None:
            self.embedding_model = SentenceTransformer(self.model_name)
    
    def _chunk_document(self, content: str) -> List[DocumentChunk]:
        """Split document into overlapping chunks."""
        chunks = []
        chunk_id = 0
        
        # Clean up the content - remove excessive whitespace but preserve structure
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        content = content.strip()
        
        start = 0
        while start < len(content):
            end = min(start + self.chunk_size, len(content))
            
            # Try to break at a natural boundary (sentence, paragraph, or word)
            if end < len(content):
                # Look for sentence boundaries first
                sentence_break = content.rfind('.', start, end)
                if sentence_break > start + self.chunk_size // 2:
                    end = sentence_break + 1
                else:
                    # Look for paragraph breaks
                    para_break = content.rfind('\n\n', start, end)
                    if para_break > start + self.chunk_size // 2:
                        end = para_break + 2
                    else:
                        # Look for line breaks
                        line_break = content.rfind('\n', start, end)
                        if line_break > start + self.chunk_size // 2:
                            end = line_break + 1
                        else:
                            # Look for word boundaries
                            word_break = content.rfind(' ', start, end)
                            if word_break > start + self.chunk_size // 2:
                                end = word_break + 1
            
            chunk_content = content[start:end].strip()
            if chunk_content:  # Only add non-empty chunks
                chunks.append(DocumentChunk(chunk_content, start, end, chunk_id))
                chunk_id += 1
            
            # Move start position with overlap
            start = max(start + 1, end - self.chunk_overlap)
            
            # Avoid infinite loop
            if start >= end:
                start = end
        
        return chunks
    
    def _get_cache_path(self, doc_path: Path, content_hash: str) -> Tuple[Path, Path]:
        """Get cache file paths for index and chunks."""
        cache_dir = doc_path.parent / ".doc_check_cache"
        cache_dir.mkdir(exist_ok=True)
        
        base_name = f"{doc_path.name}.{content_hash}.{self.model_name.replace('/', '_')}.{self.chunk_size}.{self.chunk_overlap}"
        index_path = cache_dir / f"{base_name}.index"
        chunks_path = cache_dir / f"{base_name}.chunks"
        
        return index_path, chunks_path
    
    def _load_from_cache(self, index_path: Path, chunks_path: Path) -> bool:
        """Load index and chunks from cache if available."""
        try:
            if index_path.exists() and chunks_path.exists():
                # Load FAISS index
                self.index = faiss.read_index(str(index_path))
                
                # Load chunks
                with open(chunks_path, 'rb') as f:
                    self.chunks = pickle.load(f)
                
                return True
        except Exception:
            # If loading fails, we'll rebuild
            pass
        
        return False
    
    def _save_to_cache(self, index_path: Path, chunks_path: Path):
        """Save index and chunks to cache."""
        try:
            # Save FAISS index
            faiss.write_index(self.index, str(index_path))
            
            # Save chunks
            with open(chunks_path, 'wb') as f:
                pickle.dump(self.chunks, f)
        except Exception:
            # If saving fails, just continue without caching
            pass
    
    def index_document(self, content: str, doc_path: Path) -> None:
        """Index a document for retrieval.
        
        Args:
            content: The document content to index
            doc_path: Path to the document (used for caching)
        """
        # Calculate content hash for caching
        content_hash = hashlib.sha1(content.encode('utf-8')).hexdigest()
        index_path, chunks_path = self._get_cache_path(doc_path, content_hash)
        
        # Try to load from cache first
        if self._load_from_cache(index_path, chunks_path):
            return
        
        # Load embedding model
        self._load_embedding_model()
        
        # Chunk the document
        self.chunks = self._chunk_document(content)
        
        if not self.chunks:
            raise ValueError("No valid chunks created from document")
        
        # Create embeddings for all chunks
        chunk_texts = [chunk.content for chunk in self.chunks]
        embeddings = self.embedding_model.encode(chunk_texts, convert_to_numpy=True)
        
        # Create FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings.astype(np.float32))
        
        # Save to cache
        self._save_to_cache(index_path, chunks_path)
    
    def retrieve_relevant_chunks(self, query: str, top_k: int = 5) -> List[DocumentChunk]:
        """Retrieve the most relevant chunks for a query.
        
        Args:
            query: The query to search for
            top_k: Number of top chunks to retrieve
            
        Returns:
            List of most relevant document chunks
        """
        if self.index is None or not self.chunks:
            raise ValueError("Document must be indexed before retrieval")
        
        # Load embedding model if not already loaded
        self._load_embedding_model()
        
        # Encode the query
        query_embedding = self.embedding_model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_embedding)
        
        # Search for similar chunks
        scores, indices = self.index.search(query_embedding.astype(np.float32), top_k)
        
        # Return the relevant chunks
        relevant_chunks = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.chunks):  # Valid index
                chunk = self.chunks[idx]
                relevant_chunks.append(chunk)
        
        return relevant_chunks
    
    def get_context_for_question(self, question: str, max_context_length: int = 4000) -> str:
        """Get relevant context for a question, respecting length limits.
        
        Args:
            question: The question to find context for
            max_context_length: Maximum length of context to return
            
        Returns:
            Concatenated relevant chunks as context
        """
        # Retrieve relevant chunks
        relevant_chunks = self.retrieve_relevant_chunks(question, top_k=10)
        
        # Build context string, respecting length limit
        context_parts = []
        current_length = 0
        
        for chunk in relevant_chunks:
            chunk_text = chunk.content
            if current_length + len(chunk_text) + 2 <= max_context_length:  # +2 for separator
                context_parts.append(chunk_text)
                current_length += len(chunk_text) + 2
            else:
                # Try to fit a partial chunk
                remaining_space = max_context_length - current_length - 2
                if remaining_space > 100:  # Only add if we have reasonable space
                    context_parts.append(chunk_text[:remaining_space] + "...")
                break
        
        return "\n\n".join(context_parts)
