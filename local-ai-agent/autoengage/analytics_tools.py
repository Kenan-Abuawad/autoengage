from langchain_core.tools import tool


@tool
def analyze_engagement(posts_data: list) -> str:
    """
    Analyze post engagement.
    """

    if not posts_data:
        return "No data"

    best = max(
        posts_data,
        key=lambda x: x.get("likes", 0) + x.get("comments", 0)
    )

    return (
        f"Best post: {best}\n"
        f"Reason: Highest engagement."
    )


@tool
def generate_insights(analytics: str) -> str:
    """
    Generate marketing insights.
    """

    insights = [
        "Educational posts perform well",
        "Short posts get more views",
        "Questions increase comments",
        "Visual content improves engagement",
        "CTA increases interaction"
    ]

    recommendations = [
        "Post more educational content",
        "Use stronger hooks",
        "Add visuals"
    ]

    return (
        "Insights:\n"
        + "\n".join(insights)
        + "\n\nRecommendations:\n"
        + "\n".join(recommendations)
    )


@tool
def score_lead(
    lead_name: str,
    interactions: list
) -> str:
    """
    Score a lead.
    """

    score = min(len(interactions) * 20, 100)

    if score >= 70:
        status = "hot"
    elif score >= 40:
        status = "warm"
    else:
        status = "cold"

    return (
        f"Lead: {lead_name}\n"
        f"Score: {score}\n"
        f"Status: {status}"
    )