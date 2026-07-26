import pytest

from models.response_parser import ResponseParser


sample_response = """
# Overall Score

8/10

# Bugs

None

# Performance

Good

# Security

No issues
"""


def test_parser_returns_dictionary():

    parser = ResponseParser()

    result = parser.parse(sample_response)

    assert isinstance(result, dict)


def test_parser_contains_score():

    parser = ResponseParser()

    result = parser.parse(sample_response)

    assert "Overall Score" in result


def test_parser_contains_security():

    parser = ResponseParser()

    result = parser.parse(sample_response)

    assert "Security" in result