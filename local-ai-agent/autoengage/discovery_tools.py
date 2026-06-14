from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup


@tool
def search_viral_posts(query: str, max_results: int = 5) -> str:
    """
    Search for viral posts related to a niche.
    """

    results = []

    for i in range(max_results):
        results.append(
            f"{i+1}. Example article about {query}\n"
            f"https://example{i+1}.com\n"
            f"Summary about {query}\n"
        )

    return "\n".join(results)


@tool
def read_post_content(url: str) -> str:
    """
    Read webpage content.
    """

    if not url.startswith("http"):
        return "Error: Invalid URL"

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:2000]

    except Exception as e:
        return f"Error: {e}"


@tool
def score_relevance(
    post_text: str,
    niche: str
) -> str:
    """
    Score relevance between post and niche.
    """

    keywords = niche.lower().split()

    matches = 0

    for word in keywords:
        if word in post_text.lower():
            matches += 1

    score = min(
        100,
        40 + (matches * 10)
    )

    if score >= 80:
        explanation = (
            "Highly relevant to the niche."
        )

    elif score >= 60:
        explanation = (
            "Moderately relevant to the niche."
        )

    else:
        explanation = (
            "Low relevance to the niche."
        )

    return (
        f"Score: {score}/100\n"
        f"Explanation: {explanation}"
    )