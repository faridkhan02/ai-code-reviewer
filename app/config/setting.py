"""
Application Settings
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # ==========================
    # API Keys
    # ==========================

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    # ==========================
    # Models
    # ==========================

    DEFAULT_MODEL = "gemini"

    GEMINI_MODEL = "gemini-2.5-flash"

    OPENAI_MODEL = "gpt-5.5"

    OLLAMA_MODEL = "llama3"

    # ==========================
    # App
    # ==========================

    MAX_FILE_SIZE = 5 * 1024 * 1024

    MAX_TOKENS = 4096

    TEMPERATURE = 0.2

    APP_NAME = "AI Code Reviewer"

    VERSION = "1.0.0"


settings = Settings()