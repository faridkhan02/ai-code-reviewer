import re


class SecurityChecker:

    DANGEROUS_FUNCTIONS = [
        "eval(",
        "exec(",
        "os.system(",
        "subprocess.Popen(",
        "subprocess.call(",
        "pickle.loads(",
    ]

    def __init__(self, code):
        self.code = code

    def check(self):

        issues = []

        for func in self.DANGEROUS_FUNCTIONS:
            if func in self.code:
                issues.append(f"Unsafe function detected: {func}")

        if re.search(r"password\s*=\s*['\"]", self.code):
            issues.append("Hardcoded password detected.")

        if re.search(r"api_key\s*=\s*['\"]", self.code):
            issues.append("Hardcoded API Key detected.")

        if "verify=False" in self.code:
            issues.append("SSL verification disabled.")

        return issues if issues else ["No major security issues found."]