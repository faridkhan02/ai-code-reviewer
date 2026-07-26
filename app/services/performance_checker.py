# app/services/performance_checker.py

import ast


class PerformanceChecker:

    def __init__(self, code):

        self.code = code


    def check(self):

        issues = []


        try:

            tree = ast.parse(self.code)


            for node in ast.walk(tree):


                # Detect nested loops
                if isinstance(node, ast.For):

                    for child in ast.walk(node):

                        if isinstance(child, ast.For):

                            issues.append(
                                "Nested loop detected. Performance may decrease."
                            )


                # Detect very large loops
                if isinstance(node, ast.Call):

                    if isinstance(node.func, ast.Name):

                        if node.func.id == "range":

                            if len(node.args) > 0:

                                if isinstance(node.args[0], ast.Constant):

                                    if node.args[0].value > 100000:

                                        issues.append(
                                            "Large range loop detected."
                                        )


        except Exception as e:

            issues.append(
                str(e)
            )


        return issues if issues else [
            "No performance issues detected."
        ]



# Optional direct function

def check_performance(code):

    checker = PerformanceChecker(code)

    return checker.check() 