"""
Project Constants
"""

SUPPORTED_LANGUAGES = {

    ".py": "Python",

    ".java": "Java",

    ".cpp": "C++",

    ".c": "C",

    ".js": "JavaScript",

    ".ts": "TypeScript",

    ".go": "Go",

    ".rs": "Rust",

    ".cs": "C#"

}

SUPPORTED_MODELS = [

    "Gemini",

    "OpenAI",

    "Ollama"

]

REVIEW_OPTIONS = [

    "Bug Detection",

    "Security",

    "Performance",

    "Optimization",

    "Clean Code"

]

DEFAULT_SCORE = 75

REPORT_TITLE = "AI Code Review Report"

SEPARATOR = "=" * 60