def generate_explanation(review_result):

    explanation = []

    explanation.append("# AI Code Review Summary\n")

    for section, value in review_result.items():

        explanation.append(f"## {section}")

        if isinstance(value, list):

            for item in value:
                explanation.append(f"- {item}")

        else:
            explanation.append(str(value))

        explanation.append("")

    return "\n".join(explanation) 