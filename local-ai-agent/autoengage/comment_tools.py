from langchain_core.tools import tool


@tool
def draft_comment(
    post_summary: str,
    brand_tone: str,
    cta: str
) -> str:
    """
    Generate a comment.
    """

    return (
        f"Great insights. I especially liked the point about "
        f"{post_summary[:50]}.\n\n"
        f"{cta}"
    )


@tool
def qa_check_comment(
    comment: str,
    phrases_forbidden: list
) -> dict:
    """
    Check comment quality.
    """

    forbidden_found = []

    for phrase in phrases_forbidden:
        if phrase.lower() in comment.lower():
            forbidden_found.append(phrase)

    return {
        "forbidden_check":
            "Missing" if forbidden_found else "Check",

        "forbidden_phrases":
            forbidden_found,

        "ai_smell":
            "Check",

        "value_check":
            "Check" if len(comment) > 50 else "Not Enough",

        "length_check":
            "Check" if 50 <= len(comment) <= 500 else "Not Enough"
    }