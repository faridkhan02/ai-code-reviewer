"""
LLM Integration
"""

import google.generativeai as genai

from config.settings import settings

from app.prompt import SYSTEM_PROMPT


class GeminiLLM:

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            model_name=settings.GEMINI_MODEL,
            system_instruction=SYSTEM_PROMPT
        )

    def generate_review(self, prompt):

        response = self.model.generate_content(
            prompt
        )

        return response.text


class OpenAILLM:

    def generate_review(self, prompt):

        return (
            "OpenAI integration will be added later."
        )


class OllamaLLM:

    def generate_review(self, prompt):

        return (
            "Ollama integration will be added later."
        )


class LLMFactory:

    @staticmethod
    def get_model(model_name):

        model_name = model_name.lower()

        if model_name == "gemini":

            return GeminiLLM()

        elif model_name == "openai":

            return OpenAILLM()

        elif model_name == "ollama":

            return OllamaLLM()

        else:

            raise ValueError(
                "Unsupported model selected."
            )