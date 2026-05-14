from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from web_tools import get_page_title, read_page_text

@tool
def web_title(url: str) -> str:
    """Get the title of a webpage. Use this when the user asks about a website"""
    return get_page_title(url)
@tool
def web_text(url: str) -> str:
    """Read the text of a webpage. Use this when the user asks about a website"""
    return read_page_text(url)

tools = [web_title, web_text]


def main():
    llm = ChatOllama(
        model="qwen3:8b",
        temperature=0,
    )

    tools = [web_title]

    llm_with_tools = llm.bind_tools(tools)
    messages: list[BaseMessage] = [
        SystemMessage(
            content=(
                "You are a local AI agent. "
                "You have tools available. Use them when needed. "
                "When the user asks about a website, use the web_title tool."
            )
        )
    ]

    print("=" * 50)
    print("🤖 AI Agent - Now with Web Tools!")
    print("Try: What is the title of https://example.com ?")
    print("Type 'exit' to quit.")
    print("=" * 50)
    print()
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye! 👋")
            break
        if not user_input:
            continue
        messages.append(HumanMessage(content=user_input))

        response = llm_with_tools.invoke(messages)

        tool_calls = getattr(response, "tool_calls", []) or []

        if not tool_calls:
            print(f"\nAgent: {response.content}\n")
            messages.append(response)
            continue

        messages.append(response)
        for call in tool_calls:
            tool_name = call["name"]
            tool_args = call["args"]
            matched_tool = next(t for t in tools if t.name == tool_name)
            result = matched_tool.invoke(tool_args)
            print(f"\n🔧 [Tool used: {tool_name}]")
            print(f" Result: {result}")
            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"],
                )
            )

        final_response = llm_with_tools.invoke(messages)
        print(f"\nAgent: {final_response.content}\n")
        messages.append(final_response)


if __name__ == "__main__":
    main()
