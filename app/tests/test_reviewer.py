"""
Test cases for AI Code Reviewer
"""

import sys
import os

# Add project root path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from app.reviewer import review_code



def test_review_code_basic():

    code = """
print("Hello World")
"""

    settings = {
        "ai_explanation": False
    }


    result = review_code(
        code,
        settings
    )


    assert "analysis" in result

    assert result["analysis"]["syntax"] == "Valid"



def test_review_code_with_function():

    code = """

def add(a,b):
    return a+b

"""


    settings = {
        "ai_explanation": False
    }


    result = review_code(
        code,
        settings
    )


    assert result["analysis"]["functions"] == 1



def test_review_code_bug_detection():

    code = """

try:
    x = 10

"""


    settings = {
        "ai_explanation": False
    }


    result = review_code(
        code,
        settings
    )


    bugs = result["analysis"]["bugs"]


    assert len(bugs) > 0



def test_review_code_security():

    code = """

password = "admin123"

"""


    settings = {
        "ai_explanation": False
    }


    result = review_code(
        code,
        settings
    )


    assert "security" in result["analysis"]



def test_review_code_complete_output():

    code = """

import os


class Test:

    def run(self):
        pass

"""


    settings = {
        "ai_explanation": False
    }


    result = review_code(
        code,
        settings
    )


    analysis = result["analysis"]


    assert "syntax" in analysis
    assert "bugs" in analysis
    assert "security" in analysis
    assert "performance" in analysis
    assert "style" in analysis



if __name__ == "__main__":

    test_review_code_basic()
    test_review_code_with_function()
    test_review_code_bug_detection()
    test_review_code_security()
    test_review_code_complete_output()

    print(
        "All reviewer tests passed successfully!"
    ) 