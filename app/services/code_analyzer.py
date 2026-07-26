import ast

from services.bug_detector import detect_bugs
from services.security_checker import SecurityChecker
from services.performance_checker import PerformanceChecker
from services.style_checker import StyleChecker
 



def analyze_code(code):

    result = {

        "syntax": "Valid",

        "functions": 0,

        "classes": 0,

        "imports": 0,

        "variables": 0,

        "bugs": [],

        "security": [],

        "performance": [],

        "style": [],

        "errors": []

    }


    try:

        tree = ast.parse(code)


        for node in ast.walk(tree):


            if isinstance(node, ast.FunctionDef):

                result["functions"] += 1


            elif isinstance(node, ast.ClassDef):

                result["classes"] += 1


            elif isinstance(node, ast.Import):

                result["imports"] += 1


            elif isinstance(node, ast.ImportFrom):

                result["imports"] += 1


            elif isinstance(node, ast.Assign):

                result["variables"] += 1



        # Other analyzers

        result["bugs"] = detect_bugs(code)


        result["security"] = SecurityChecker(
            code
        ).check()


        result["performance"] = PerformanceChecker(
            code
        ).check()


        result["style"] = StyleChecker(
            code
        ).check()



    except SyntaxError as e:

        result["syntax"] = "Invalid"

        result["errors"].append(
            str(e)
        )


    return result 