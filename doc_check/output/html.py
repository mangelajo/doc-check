"""HTML output formatter for doc-check results."""

from pathlib import Path
from typing import Optional
from datetime import datetime

import markdown

from .base import OutputFormatter
from ..models import DocCheckResult


class HTMLFormatter(OutputFormatter):
    """HTML output formatter."""
    
    @property
    def default_filename(self) -> str:
        return "doc-check-results"
    
    @property
    def file_extension(self) -> str:
        return ".html"
    
    def write_results(self, result: DocCheckResult, filename: Optional[str] = None) -> Path:
        """Write results as HTML file."""
        if filename is None:
            filename = self.default_filename
        
        if not filename.endswith(self.file_extension):
            filename += self.file_extension
        
        output_path = self.output_dir / filename
        
        html_content = self._generate_html(result)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_path
    
    def _generate_html(self, result: DocCheckResult) -> str:
        """Generate HTML content for the results."""
        # Determine overall status
        overall_status = "PASS" if result.failed_questions == 0 else "FAIL"
        status_class = "pass" if overall_status == "PASS" else "fail"
        
        # Format timestamps
        start_time_str = result.start_time.strftime("%Y-%m-%d %H:%M:%S") if result.start_time else "N/A"
        end_time_str = result.end_time.strftime("%Y-%m-%d %H:%M:%S") if result.end_time else "N/A"
        duration_str = f"{result.duration_seconds:.1f}s" if result.duration_seconds else "N/A"
        
        # Generate summary table HTML
        summary_rows = []
        detailed_sections = []
        
        for i, question_result in enumerate(result.results, 1):
            status = "PASS" if question_result.passed else "FAIL"
            status_class_row = "pass" if question_result.passed else "fail"
            status_icon = "✓" if question_result.passed else "✗"
            
            if question_result.error:
                evaluation_summary = f"Error: {self._escape_html(question_result.error)}"
                evaluation_full = evaluation_summary
            else:
                evaluation_full = self._escape_html(question_result.evaluation_result)
                # Create a shorter summary for the table
                evaluation_summary = evaluation_full[:100] + "..." if len(evaluation_full) > 100 else evaluation_full
            
            # Summary table row
            summary_rows.append(f"""
                <tr class="{status_class_row}">
                    <td>{i}</td>
                    <td><a href="#question-{i}" class="question-link">{self._escape_html(question_result.name)}</a></td>
                    <td class="status {status_class_row}">
                        <span class="icon {status_class_row}-icon">{status_icon}</span>
                        {status}
                    </td>
                    <td class="evaluation-summary">{evaluation_summary}</td>
                </tr>
            """)
            
            # Detailed section
            detailed_sections.append(f"""
                <div class="question-detail {status_class_row}" id="question-{i}">
                    <div class="question-header">
                        <h3>Question {i}: {self._escape_html(question_result.name)}</h3>
                        <div class="status-badge {status_class_row}">
                            <span class="icon {status_class_row}-icon">{status_icon}</span>
                            {status}
                        </div>
                    </div>
                    <div class="question-content">
                        <div class="question-block">
                            <h4>Question</h4>
                            <div class="question-text">{self._escape_html(question_result.question)}</div>
                        </div>
                        <div class="answer-block">
                            <h4>Answer</h4>
                            <div class="answer-text">{self._detect_and_convert_content(question_result.answer)}</div>
                        </div>
                        <div class="evaluation-block">
                            <h4>Evaluation</h4>
                            <div class="evaluation-text">{self._detect_and_convert_content(question_result.evaluation_result)}</div>
                        </div>
                    </div>
                </div>
            """)
        
        # API usage section
        api_usage_html = ""
        if result.api_usage:
            usage = result.api_usage
            api_usage_html = f"""
                <div class="section">
                    <h2>API Usage</h2>
                    <div class="stats-grid">
                        <div class="stat">
                            <span class="label">Provider:</span>
                            <span class="value">{self._escape_html(usage.provider)}</span>
                        </div>
                        <div class="stat">
                            <span class="label">Model:</span>
                            <span class="value">{self._escape_html(usage.model)}</span>
                        </div>
                        <div class="stat">
                            <span class="label">API Calls:</span>
                            <span class="value">{usage.api_calls}</span>
                        </div>
                        <div class="stat">
                            <span class="label">Total Tokens:</span>
                            <span class="value">{usage.total_tokens:,}</span>
                        </div>
                        <div class="stat">
                            <span class="label">Input Tokens:</span>
                            <span class="value">{usage.input_tokens:,}</span>
                        </div>
                        <div class="stat">
                            <span class="label">Output Tokens:</span>
                            <span class="value">{usage.output_tokens:,}</span>
                        </div>
                        <div class="stat">
                            <span class="label">Estimated Cost:</span>
                            <span class="value">${usage.estimated_cost:.4f}</span>
                        </div>
                    </div>
                </div>
            """
        
        # Summarization info
        summarization_html = ""
        if result.summarization_level:
            summarization_html = f"""
                <div class="stat">
                    <span class="label">Summarization Level:</span>
                    <span class="value">{result.summarization_level}</span>
                </div>
            """
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doc-Check Results - {overall_status}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .status-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 10px;
            font-size: 1.1em;
        }}
        .status-badge.pass {{
            background-color: #4CAF50;
        }}
        .status-badge.fail {{
            background-color: #f44336;
        }}
        .section {{
            padding: 30px;
            border-bottom: 1px solid #eee;
        }}
        .section:last-child {{
            border-bottom: none;
        }}
        .section h2 {{
            margin-top: 0;
            color: #333;
            font-size: 1.5em;
            font-weight: 500;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .stat {{
            display: flex;
            justify-content: space-between;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 6px;
            border-left: 4px solid #667eea;
        }}
        .stat .label {{
            font-weight: 700;
            color: #333;
        }}
        .stat .value {{
            color: #333;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .icon {{
            font-weight: bold;
            font-size: 1.1em;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: white;
        }}
        .pass-icon {{
            background-color: #4CAF50;
        }}
        .fail-icon {{
            background-color: #f44336;
        }}
        .progress-bar {{
            position: relative;
            width: 100px;
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #f44336 0%, #ff9800 50%, #4CAF50 100%);
            transition: width 0.3s ease;
        }}
        .progress-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 0.8em;
            font-weight: bold;
            color: #333;
            text-shadow: 1px 1px 1px rgba(255,255,255,0.8);
        }}
        .results-bar {{
            margin: 20px 0 30px 0;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border: 1px solid #dee2e6;
        }}
        .bar-container {{
            display: flex;
            height: 40px;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }}
        .bar-segment {{
            transition: width 0.5s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }}
        .pass-segment {{
            background: linear-gradient(135deg, #4CAF50, #45a049);
        }}
        .fail-segment {{
            background: linear-gradient(135deg, #f44336, #e53935);
        }}
        .bar-labels {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .bar-label {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
            font-size: 1.1em;
        }}
        .pass-label {{
            color: #4CAF50;
        }}
        .fail-label {{
            color: #f44336;
        }}
        .success-rate {{
            color: #667eea;
            font-weight: 700;
        }}
        .results-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        .results-table th {{
            background-color: #f8f9fa;
            padding: 15px 10px;
            text-align: left;
            font-weight: 600;
            color: #555;
            border-bottom: 2px solid #dee2e6;
        }}
        .results-table td {{
            padding: 15px 10px;
            border-bottom: 1px solid #dee2e6;
            vertical-align: top;
        }}
        .results-table tr.pass {{
            background-color: #f8fff8;
        }}
        .results-table tr.fail {{
            background-color: #fff8f8;
        }}
        .status {{
            font-weight: bold;
            padding: 4px 8px;
            border-radius: 4px;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }}
        .status.pass {{
            background-color: #4CAF50;
            color: white;
        }}
        .status.fail {{
            background-color: #f44336;
            color: white;
        }}
        .evaluation-summary {{
            max-width: 400px;
            word-wrap: break-word;
            font-size: 0.9em;
            line-height: 1.4;
            color: #555;
        }}
        .question-link {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }}
        .question-link:hover {{
            color: #764ba2;
            text-decoration: underline;
        }}
        .question-detail {{
            margin: 30px 0;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            overflow: hidden;
        }}
        .question-detail.pass {{
            border-left: 4px solid #4CAF50;
        }}
        .question-detail.fail {{
            border-left: 4px solid #f44336;
        }}
        .question-header {{
            background-color: #f8f9fa;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #dee2e6;
        }}
        .question-header h3 {{
            margin: 0;
            color: #333;
            font-size: 1.2em;
        }}
        .question-content {{
            padding: 20px;
        }}
        .question-block, .answer-block, .evaluation-block {{
            margin-bottom: 25px;
        }}
        .question-block:last-child, .answer-block:last-child, .evaluation-block:last-child {{
            margin-bottom: 0;
        }}
        .question-block h4, .answer-block h4, .evaluation-block h4 {{
            margin: 0 0 10px 0;
            color: #555;
            font-size: 1em;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .question-text, .answer-text, .evaluation-text {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 6px;
            line-height: 1.6;
            word-wrap: break-word;
        }}
        .question-text {{
            white-space: pre-wrap;
        }}
        .answer-text, .evaluation-text {{
            /* Allow HTML content for markdown conversion */
        }}
        .answer-text h1, .answer-text h2, .answer-text h3,
        .evaluation-text h1, .evaluation-text h2, .evaluation-text h3 {{
            margin: 0.5em 0;
            color: #333;
        }}
        .answer-text code, .evaluation-text code {{
            background-color: #e9ecef;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 0.9em;
        }}
        .answer-text pre, .evaluation-text pre {{
            background-color: #e9ecef;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
            margin: 10px 0;
        }}
        .answer-text pre code, .evaluation-text pre code {{
            background: none;
            padding: 0;
        }}
        .answer-text ul, .answer-text ol,
        .evaluation-text ul, .evaluation-text ol {{
            margin: 10px 0;
            padding-left: 20px;
        }}
        .answer-text li, .evaluation-text li {{
            margin: 5px 0;
        }}
        .answer-text p, .evaluation-text p {{
            margin: 10px 0;
        }}
        .answer-text a, .evaluation-text a {{
            color: #667eea;
            text-decoration: none;
        }}
        .answer-text a:hover, .evaluation-text a:hover {{
            text-decoration: underline;
        }}
        .answer-text strong, .evaluation-text strong {{
            font-weight: 600;
        }}
        .answer-text em, .evaluation-text em {{
            font-style: italic;
        }}
        /* Table styles for markdown tables */
        .answer-text table, .evaluation-text table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            border: 1px solid #dee2e6;
        }}
        .answer-text th, .answer-text td,
        .evaluation-text th, .evaluation-text td {{
            border: 1px solid #dee2e6;
            padding: 8px 12px;
            text-align: left;
        }}
        .answer-text th, .evaluation-text th {{
            background-color: #f8f9fa;
            font-weight: 600;
        }}
        .answer-text tr:nth-child(even), .evaluation-text tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        /* Blockquote styles */
        .answer-text blockquote, .evaluation-text blockquote {{
            border-left: 4px solid #667eea;
            margin: 15px 0;
            padding: 10px 15px;
            background-color: #f8f9fa;
            font-style: italic;
        }}
        /* Horizontal rule styles */
        .answer-text hr, .evaluation-text hr {{
            border: none;
            border-top: 2px solid #dee2e6;
            margin: 20px 0;
        }}
        /* Error/fallback styles */
        .markdown-error {{
            border: 1px solid #ffc107;
            background-color: #fff3cd;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
        }}
        .markdown-error p {{
            margin: 0 0 10px 0;
            color: #856404;
        }}
        .question-text {{
            font-style: italic;
            color: #666;
            border-left: 3px solid #667eea;
        }}
        .answer-text {{
            color: #333;
            border-left: 3px solid #28a745;
        }}
        .evaluation-text {{
            color: #555;
            border-left: 3px solid #ffc107;
        }}
        .timestamp {{
            color: #666;
            font-size: 0.9em;
            text-align: center;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Doc-Check Results</h1>
            <div class="status-badge {status_class}">{overall_status}</div>
        </div>
        
        <div class="section">
            <h2>Summary</h2>
            <div class="results-bar">
                <div class="bar-container">
                    <div class="bar-segment pass-segment" style="width: {result.success_rate}%"></div>
                    <div class="bar-segment fail-segment" style="width: {100 - result.success_rate}%"></div>
                </div>
                <div class="bar-labels">
                    <div class="bar-label pass-label">
                        <span class="icon pass-icon">✓</span>
                        Passed: {result.passed_questions}
                    </div>
                    <div class="bar-label success-rate">
                        Success Rate: {result.success_rate:.1f}%
                    </div>
                    <div class="bar-label fail-label">
                        <span class="icon fail-icon">✗</span>
                        Failed: {result.failed_questions}
                    </div>
                </div>
            </div>
            <div class="stats-grid">
                <div class="stat">
                    <span class="label">Total Questions:</span>
                    <span class="value">{result.total_questions}</span>
                </div>
                <div class="stat">
                    <span class="label">Duration:</span>
                    <span class="value">{duration_str}</span>
                </div>
                <div class="stat">
                    <span class="label">Start Time:</span>
                    <span class="value">{start_time_str}</span>
                </div>
                <div class="stat">
                    <span class="label">End Time:</span>
                    <span class="value">{end_time_str}</span>
                </div>
                {summarization_html}
            </div>
        </div>
        
        {api_usage_html}
        
        <div class="section">
            <h2>Results Summary</h2>
            <table class="results-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Status</th>
                        <th>Evaluation Summary</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(summary_rows)}
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h2>Detailed Results</h2>
            {''.join(detailed_sections)}
        </div>
        
        <div class="timestamp">
            Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </div>
    </div>
</body>
</html>"""
    
    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters."""
        if not text:
            return ""
        return (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#x27;"))
    
    def _detect_and_convert_content(self, text: str) -> str:
        """Detect content type and convert to HTML if needed."""
        if not text:
            return ""
        
        # Check if content looks like markdown
        if self._is_markdown(text):
            return self._convert_markdown_to_html(text)
        else:
            # Regular text, just escape HTML
            return self._escape_html(text)
    
    def _is_markdown(self, text: str) -> bool:
        """Detect if text contains markdown formatting."""
        import re
        markdown_patterns = [
            r'^#{1,6}\s+',  # Headers
            r'\*\*.*?\*\*',  # Bold
            r'\*.*?\*',  # Italic
            r'`.*?`',  # Inline code
            r'^```',  # Code blocks
            r'^\* ',  # Unordered lists
            r'^\d+\. ',  # Ordered lists
            r'^\- ',  # Alternative unordered lists
            r'\[.*?\]\(.*?\)',  # Links
            r'^\|.*\|.*\|',  # Tables
        ]
        
        for pattern in markdown_patterns:
            if re.search(pattern, text, re.MULTILINE):
                return True
        return False
    
    def _convert_markdown_to_html(self, text: str) -> str:
        """Convert markdown to HTML using the markdown library."""
        try:
            # Configure markdown with useful extensions
            md = markdown.Markdown(extensions=[
                'tables',           # Support for tables
                'fenced_code',      # Support for ```code``` blocks
                'codehilite',       # Syntax highlighting for code
                'nl2br',            # Convert newlines to <br>
                'toc',              # Table of contents
                'attr_list',        # Attribute lists {: .class}
                'def_list',         # Definition lists
                'abbr',             # Abbreviations
                'footnotes',        # Footnotes
            ], extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'use_pygments': False,  # Use CSS classes instead of inline styles
                }
            })
            
            # Convert markdown to HTML
            html = md.convert(text)
            return html
            
        except Exception as e:
            # If markdown conversion fails, fall back to escaped text
            return f'<div class="markdown-error"><p><em>Error converting markdown: {self._escape_html(str(e))}</em></p><pre>{self._escape_html(text)}</pre></div>'
