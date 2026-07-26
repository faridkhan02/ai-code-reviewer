import pytest

from services.code_analyzer import CodeAnalyzer
from services.security_checker import SecurityChecker
from services.bug_detector import BugDetector
from services.performance_checker import PerformanceChecker
from services.style_checker import StyleChecker
from services.explanation_service import ExplanationService


code = """
import os

def hello():
    print("Hello")
"""


def test_complete_pipeline():

    analysis = CodeAnalyzer(code).analyze()

    security = SecurityChecker(code).check()

    bugs = BugDetector(code).detect()

    performance = PerformanceChecker(code).check()

    style = StyleChecker(code).check()

    report = {
        "Analysis": analysis,
        "Security": security,
        "Bugs": bugs,
        "Performance": performance,
        "Style": style,
    }

    summary = ExplanationService().explain(report)

    assert isinstance(summary, str)
    assert "Analysis" in summary


def test_analyzer():

    result = CodeAnalyzer(code).analyze()

    assert result["syntax"] == "Valid"


def test_security():

    result = SecurityChecker(code).check()

    assert isinstance(result, list)


def test_bug_detector():

    result = BugDetector(code).detect()

    assert isinstance(result, list)


def test_performance():

    result = PerformanceChecker(code).check()

    assert isinstance(result, list)


def test_style():

    result = StyleChecker(code).check()

    assert isinstance(result, list)