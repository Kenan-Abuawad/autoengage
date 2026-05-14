from langchain_ollama import ChatOllama
from my_tools import calculate, add_task, get_tasks, get_time

SYSTEM_PROMPT = (
    "You are a capable personal assistant. "
    "You can do math (calculate), manage a simple task list (add_task, get_tasks), "
    "and report the current time (get_time). "
    "Use tools when they help answer the user; otherwise reply directly."
)

llm = ChatOllama(model="qwen3:8b")

tools = [calculate, add_task, get_tasks, get_time]

llm_with_tools = llm.bind_tools(tools)

messages = [
 {"role": "system", "content": SYSTEM_PROMPT}
]

tool_map = {
 "calculate": calculate,
 "add_task": add_task,
 "get_tasks": get_tasks,
 "get_time": get_time,
}

