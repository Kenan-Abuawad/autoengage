from langchain_core.tools import tool
from datetime import datetime

tasks = []

@tool
def calculate(expression: str) -> str:
    """Calculate the result of a mathematical expression"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

@tool
def add_task(task: str) -> str:
    """Add a task to the list of tasks"""
    tasks.append(task)
    return f"Task added: {task}"

@tool
def get_tasks() -> str:
    """Return all tasks currently in the list."""
    if not tasks:
        return "No tasks yet."
    return "\n".join(f"{i + 1}. {t}" for i, t in enumerate(tasks))


@tool
def get_time() -> str:
    """Return the current local date and time as an ISO 8601 string."""
    return datetime.now().isoformat(timespec="seconds")

if __name__ == "__main__":
 print("=== Testing tools ===")
 print(calculate.invoke({"expression": "100 * 0.85"}))
 print(add_task.invoke({"task": "Test task"}))
 print(get_tasks.invoke({}))
 print(get_time.invoke({}))
 print("=== All tools work! ===")