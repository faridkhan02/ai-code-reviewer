# app/services/bug_detector.py

import ast


class BugDetector:

    def __init__(self, code):

        self.code = code


    def detect(self):

        bugs = []


        try:

            tree = ast.parse(self.code)


            for node in ast.walk(tree):


                # try without except
                if isinstance(node, ast.Try):

                    if len(node.handlers) == 0:

                        bugs.append(
                            "Try block without except."
                        )


                # bare except
                if isinstance(node, ast.ExceptHandler):

                    if node.type is None:

                        bugs.append(
                            "Generic except detected."
                        )


        except SyntaxError as e:

            bugs.append(
                f"Syntax Error: {e}"
            )


        return bugs if bugs else [
            "No common bugs detected."
        ]



# IMPORTANT FUNCTION
# code_analyzer.py uses this

def detect_bugs(code):

    detector = BugDetector(code)

    return detector.detect() 