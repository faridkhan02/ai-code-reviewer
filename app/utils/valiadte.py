from pathlib import Path


class Validator:

    SUPPORTED_EXTENSIONS = {
        ".py",
        ".java",
        ".cpp",
        ".c",
        ".js",
        ".ts",
        ".go",
        ".php",
        ".cs",
        ".rb",
    }

    @staticmethod
    def validate_file(file):

        if file is None:
            return False, "No file selected."

        extension = Path(file.name).suffix.lower()

        if extension not in Validator.SUPPORTED_EXTENSIONS:
            return (
                False,
                f"Unsupported file type: {extension}",
            )

        return True, "Valid file."

    @staticmethod
    def validate_code(code):

        if not code:
            return False, "Code is empty."

        if len(code.strip()) == 0:
            return False, "Code contains only whitespace."

        return True, "Valid code."