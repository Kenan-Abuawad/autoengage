from langchain_core.tools import tool


@tool
def generate_post_ideas(
    niche: str,
    count: int = 5
) -> str:
    """
    Generate post ideas.
    """

    ideas = []

    for i in range(count):
        ideas.append(
            f"{i+1}. Content idea about {niche}"
        )

    return "\n".join(ideas)


@tool
def write_post(
    idea: str,
    platform: str,
    tone: str
) -> str:
    """
    Write a platform-specific post.
    """

    platform = platform.lower()

    if platform == "linkedin":
        return (
            f"🚀 {idea}\n\n"
            f"Professional insight.\n"
            f"Tone: {tone}"
        )

    if platform == "reddit":
        return (
            f"{idea}\n\n"
            f"What do you think about this?"
        )

    if platform == "twitter":
        post = f"{idea} | {tone}"
        return post[:280]

    return f"{idea}\nTone: {tone}"


@tool
def suggest_visual(post_text: str) -> str:
    """
    Suggest visuals for a post.
    """

    return (
        "1. Infographic\n"
        "2. Before and after comparison\n"
        "3. Professional illustration"
    )


@tool
def ab_test_versions(
    idea: str,
    tone: str
) -> str:
    """
    Create A/B test post versions.
    """

    version_a = (
        f"A Version:\n"
        f"{idea}\n"
        f"Educational style."
    )

    version_b = (
        f"B Version:\n"
        f"{idea}\n"
        f"Storytelling style."
    )

    return (
        f"{version_a}\n\n"
        f"{version_b}\n\n"
        f"Difference: A teaches, B tells a story."
    )