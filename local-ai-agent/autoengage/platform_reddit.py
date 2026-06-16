from langchain_core.tools import tool


@tool
def reddit_search_posts(
    subreddit: str,
    query: str,
    limit: int = 10
) -> str:
    """
    Search Reddit posts.
    """
    return "Reddit module skipped by instructor."


@tool
def reddit_read_post(
    post_url: str
) -> str:
    """
    Read a Reddit post.
    """
    return "Reddit module skipped by instructor."


@tool
def reddit_post_comment(
    post_url: str,
    comment_text: str
) -> str:
    """
    Publish a Reddit comment.
    """
    return "Reddit module skipped by instructor."


@tool
def reddit_monitor_replies(
    username: str
) -> str:
    """
    Monitor Reddit replies.
    """
    return "Reddit module skipped by instructor."