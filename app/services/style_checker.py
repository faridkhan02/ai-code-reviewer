import re


class StyleChecker:

    def __init__(self, code):
        self.code = code

    def check(self):

        issues = []

        lines = self.code.splitlines()

        for index, line in enumerate(lines, start=1):

            if len(line) > 88:
                issues.append(f"Line {index}: exceeds 88 characters.")

            if "\t" in line:
                issues.append(f"Line {index}: contains tab indentation.")

        if re.search(r"[A-Z]{2,}", self.code):
            issues.append("Variable naming may not follow snake_case.")

        return issues if issues else ["Style follows PEP8 reasonably well."]