"""JUnit XML output formatter for doc-check results."""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional
from datetime import datetime

from .base import OutputFormatter
from ..models import DocCheckResult


class JUnitFormatter(OutputFormatter):
    """JUnit XML output formatter."""
    
    @property
    def default_filename(self) -> str:
        return "doc-check-results"
    
    @property
    def file_extension(self) -> str:
        return ".xml"
    
    def write_results(self, result: DocCheckResult, filename: Optional[str] = None) -> Path:
        """Write results as JUnit XML file."""
        if filename is None:
            filename = self.default_filename
        
        if not filename.endswith(self.file_extension):
            filename += self.file_extension
        
        output_path = self.output_dir / filename
        
        xml_content = self._generate_junit_xml(result)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        return output_path
    
    def _generate_junit_xml(self, result: DocCheckResult) -> str:
        """Generate JUnit XML content for the results."""
        # Create root testsuite element
        testsuite = ET.Element("testsuite")
        testsuite.set("name", "doc-check")
        testsuite.set("tests", str(result.total_questions))
        testsuite.set("failures", str(result.failed_questions))
        testsuite.set("errors", "0")  # We don't distinguish between failures and errors
        testsuite.set("skipped", "0")
        
        # Add timing information if available
        if result.duration_seconds:
            testsuite.set("time", f"{result.duration_seconds:.3f}")
        
        # Add timestamp if available
        if result.start_time:
            testsuite.set("timestamp", result.start_time.isoformat())
        
        # Add hostname (optional)
        testsuite.set("hostname", "localhost")
        
        # Add properties section with metadata
        properties = ET.SubElement(testsuite, "properties")
        
        if result.api_usage:
            usage = result.api_usage
            self._add_property(properties, "api.provider", usage.provider)
            self._add_property(properties, "api.model", usage.model)
            self._add_property(properties, "api.calls", str(usage.api_calls))
            self._add_property(properties, "api.total_tokens", str(usage.total_tokens))
            self._add_property(properties, "api.input_tokens", str(usage.input_tokens))
            self._add_property(properties, "api.output_tokens", str(usage.output_tokens))
            self._add_property(properties, "api.estimated_cost", f"{usage.estimated_cost:.4f}")
        
        if result.summarization_level:
            self._add_property(properties, "summarization.level", result.summarization_level)
        
        self._add_property(properties, "success_rate", f"{result.success_rate:.1f}%")
        
        # Add test cases
        for question_result in result.results:
            testcase = ET.SubElement(testsuite, "testcase")
            testcase.set("name", question_result.name)
            testcase.set("classname", "doc-check")
            
            # Add timing if we had per-question timing (we don't currently track this)
            # testcase.set("time", "0.000")
            
            if not question_result.passed:
                if question_result.error:
                    # This was an error (exception occurred)
                    error = ET.SubElement(testcase, "error")
                    error.set("type", "ProcessingError")
                    error.set("message", question_result.error)
                    error.text = f"Question: {question_result.question}\nError: {question_result.error}"
                else:
                    # This was a failure (evaluation failed)
                    failure = ET.SubElement(testcase, "failure")
                    failure.set("type", "EvaluationFailure")
                    failure.set("message", "Question evaluation failed")
                    failure.text = f"Question: {question_result.question}\nAnswer: {question_result.answer}\nEvaluation: {question_result.evaluation_result}"
            
            # Add system-out with question details
            system_out = ET.SubElement(testcase, "system-out")
            system_out.text = f"Question: {question_result.question}\nAnswer: {question_result.answer}\nEvaluation: {question_result.evaluation_result}"
        
        # Convert to string with proper XML declaration
        xml_str = ET.tostring(testsuite, encoding='unicode', method='xml')
        return f'<?xml version="1.0" encoding="UTF-8"?>\n{xml_str}'
    
    def _add_property(self, properties_element: ET.Element, name: str, value: str) -> None:
        """Add a property element to the properties section."""
        prop = ET.SubElement(properties_element, "property")
        prop.set("name", name)
        prop.set("value", value)
