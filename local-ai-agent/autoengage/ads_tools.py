from langchain_core.tools import tool

from discovery_tools import (
    search_viral_posts,
    read_post_content
)


@tool
def research_competitor_ads(
    competitor_name: str
) -> str:
    """
    Research competitor advertising style.
    """

    try:
        results = search_viral_posts.invoke({
            "query": competitor_name,
            "max_results": 3
        })

        return (
            f"Competitor: {competitor_name}\n\n"
            f"Research Results:\n{results}\n\n"
            f"Observed Style:\n"
            f"- Educational marketing\n"
            f"- Problem/Solution format\n"
            f"- CTA at the end"
        )

    except Exception as e:
        return f"Error: {e}"


@tool
def extract_ad_patterns(
    data_ads: str
) -> str:
    """
    Extract repeating advertising patterns.
    """

    patterns = [
        "Strong hook in first sentence",
        "Problem → Solution structure",
        "Customer-focused messaging",
        "Clear CTA",
        "Short paragraphs"
    ]

    return "\n".join(
        f"{i+1}. {pattern}"
        for i, pattern in enumerate(patterns)
    )


@tool
def suggest_ad_copy(
    patterns: str,
    brand_tone: str
) -> str:
    """
    Generate ad copy ideas.
    """

    ad_1 = (
        "Ad Version 1\n"
        "Save time with AI automation.\n"
        "See how your business can work smarter."
    )

    ad_2 = (
        "Ad Version 2\n"
        "Still doing repetitive tasks manually?\n"
        "Let AI handle the busy work."
    )

    ad_3 = (
        "Ad Version 3\n"
        "AI made simple for small businesses.\n"
        "Start improving productivity today."
    )

    return (
        f"Brand Tone: {brand_tone}\n\n"
        f"{ad_1}\n\n"
        f"{ad_2}\n\n"
        f"{ad_3}"
    )