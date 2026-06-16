from langchain_core.tools import tool


@tool
def analyze_engagement(posts_data) -> str:
    """
    Analyze post engagement.
    """

    if not isinstance(posts_data, list):
        return (
            "No structured analytics data provided.\n"
            "Expected a list of posts with likes and comments."
        )

    if not posts_data:
        return "No data available."

    valid_posts = []

    for post in posts_data:
        if isinstance(post, dict):
            valid_posts.append(post)

    if not valid_posts:
        return (
            "No valid post data found.\n"
            "Expected dictionaries containing likes and comments."
        )

    try:
        best = max(
            valid_posts,
            key=lambda x: x.get("likes", 0) + x.get("comments", 0)
        )

        engagement = (
            best.get("likes", 0)
            + best.get("comments", 0)
        )

        return (
            f"Best post: {best}\n"
            f"Total engagement: {engagement}\n"
            f"Reason: Highest engagement score."
        )

    except Exception as e:
        return f"Analytics error: {e}"


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
    interactions
) -> str:
    """
    Score a lead.
    """

    if interactions is None:
        interactions = []

    if not isinstance(interactions, list):
        interactions = [str(interactions)]

    score = min(len(interactions) * 20, 100)

    if score >= 70:
        status = "hot"
    elif score >= 40:
        status = "warm"
    else:
        status = "cold"

    return (
        f"Lead: {lead_name}\n"
        f"Interactions: {len(interactions)}\n"
        f"Score: {score}/100\n"
        f"Status: {status}"
    )