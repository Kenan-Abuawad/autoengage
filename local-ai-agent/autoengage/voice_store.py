from langchain_core.tools import tool

voice_samples = []


@tool
def add_voice_sample(text: str, category: str = "general") -> str:
    """
    Save writing style sample.
    """

    voice_samples.append({
        "text": text,
        "category": category
    })

    return "Voice sample saved."


@tool
def find_similar_voice(
    query: str,
    category: str,
    k: int = 3
) -> str:
    """
    Find similar voice examples.
    """

    matches = []

    for sample in voice_samples:
        if sample["category"] == category:
            matches.append(sample["text"])

    return "\n\n".join(matches[:k])