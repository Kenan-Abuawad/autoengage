from langchain_core.tools import tool

@tool
def check_forbidden_phrases(
    text: str,
    forbidden: list
) -> str:
    """
    Check forbidden phrases.
    """

    found = []

    for phrase in forbidden:
        if phrase.lower() in text.lower():
            found.append(phrase)

    if found:
        return f"Found: {', '.join(found)}" 

    return "Passed"


@tool
def check_ai_smell(text: str) -> str:
    """
    Estimate AI smell score.
    """

    score = 2

    if "revolutionary" in text.lower():
        score += 3

    if len(text) > 1000:
        score += 2

    return (
        f"AI Smell Score: {score}/10"
    )


@tool
def fact_check(text: str) -> str:
    """
    Simple fact check.
    """

    return (
        "Error: Unable to verify facts automatically.\n"
        "Manual review recommended."
    )


@tool
def overall_quality_score(
    text: str,
    forbidden: list
) -> str:
    """
    Overall quality score.
    """

    score = 100

    for phrase in forbidden:
        if phrase.lower() in text.lower():
            score -= 20

    if len(text) < 50:
        score -= 20

    return f"Quality Score: {score}/100"