from app.services.code_analyzer import analyze_code
from app.services.explanation_service import generate_explanation


def review_code(code, settings):
    analysis = analyze_code(code)

    explanation = ""
    if settings.get("ai_explanation"):
        explanation = generate_explanation(analysis)

    return {
        "analysis": analysis,
        "explanation": explanation,
    }
