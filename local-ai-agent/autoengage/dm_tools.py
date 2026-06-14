from langchain_core.tools import tool

conversation_log = []


@tool
def identify_warm_leads(interactions: list) -> str:
    """
    Identify warm leads from interactions.
    """

    results = []

    for item in interactions:
        score = 0

        text = str(item).lower()

        if "question" in text:
            score += 50

        if "comment" in text:
            score += 30

        if "like" in text:
            score += 10

        results.append(
            f"{item} | Score: {score}"
        )

    return "\n".join(results)


@tool
def draft_dm(
    lead_name: str,
    context: str,
    brand_tone: str
) -> str:
    """
    Create a personalized DM.
    """

    return (
        f"Hi {lead_name},\n\n"
        f"I noticed you {context}. "
        f"Thought you might find our AI automation ideas useful.\n\n"
        f"Tone: {brand_tone}"
    )


@tool
def track_conversation(
    lead_name: str,
    message: str,
    status: str
) -> str:
    """
    Save conversation status.
    """

    conversation_log.append({
        "lead": lead_name,
        "message": message,
        "status": status
    })

    return f"Conversation saved for {lead_name}"