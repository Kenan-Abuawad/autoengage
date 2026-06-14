from langchain_core.tools import tool


@tool
def linkedin_search_posts(
    query: str,
    results_max: int = 5
) -> str:
    """
    Search LinkedIn posts.
    """

    results = []

    for i in range(results_max):
        results.append(
            f"{i+1}. LinkedIn post about {query}"
        )

    return "\n".join(results)


@tool
def linkedin_read_post(
    post_url: str
) -> str:
    """
    Read LinkedIn post.
    """

    return f"Content from {post_url}"


@tool
def linkedin_post_comment(
    post_url: str,
    comment_text: str
) -> str:
    """
    Publish LinkedIn comment.
    """

    return (
        f"Comment published on {post_url}"
    )