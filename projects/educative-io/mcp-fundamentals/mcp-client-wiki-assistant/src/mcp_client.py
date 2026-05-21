import asyncio

# These classes help us manage the MCP client connection and define how the server will be launched.
from mcp import ClientSession, StdioServerParameters 


from mcp.client.stdio import stdio_client
from langgraph.graph import StateGraph, START, END

# LangGraph utilities for message handling and state management
from langgraph.graph.message import AnyMessage, add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import tools_condition, ToolNode

# typing utilities in Python. List defines that the messages field will 
# contain a list of elements, and Annotated let us attach metadata
from typing import Annotated, List

# 
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_mcp_adapters.tools import load_mcp_tools

# Defining server connection parameters
# The MCP server runs as a local subprocess using standard input/output (stdio) 
# as the transport layer. We define the server’s command and arguments using StdioServerParameters.
# MCP server launch config
server_params = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)

# LangGraph state definition
class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]


# Creating the LangGraph graph
# This function sets up the LangGraph graph that orchestrates the agent’s behavior.
# It defines the nodes (chat_node and tool_node) and the edges (conditional routing based on tool usage).
# The graph is compiled with a memory checkpoint to persist state between invocations.
async def create_graph(session):
    # Load tools from MCP server
    tools = await load_mcp_tools(session)

    # LLM configuration (system prompt can be added later)
    llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key="{{OPENAI_API_KEY}}")
    llm_with_tools = llm.bind_tools(tools)

    # Prompt template with user/assistant chat only
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that uses tools to search Wikipedia."),
        MessagesPlaceholder("messages")
    ])

    chat_llm = prompt_template | llm_with_tools

    # Define chat node
    def chat_node(state: State) -> State:
        state["messages"] = chat_llm.invoke({"messages": state["messages"]})
        return state

    # Build LangGraph with tool routing
    graph = StateGraph(State)
    graph.add_node("chat_node", chat_node)
    graph.add_node("tool_node", ToolNode(tools=tools))
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition, {
        "tools": "tool_node",
        "__end__": END
    })
    graph.add_edge("tool_node", "chat_node")

    return graph.compile(checkpointer=MemorySaver())


# Entry point
async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            agent = await create_graph(session)
            print("Wikipedia MCP agent is ready.")

            while True:
                user_input = input("\nYou: ").strip()
                if user_input.lower() in {"exit", "quit", "q"}:
                    break

                try:
                    response = await agent.ainvoke(
                        {"messages": user_input},
                        config={"configurable": {"thread_id": "wiki-session"}}
                    )
                    print("AI:", response["messages"][-1].content)
                except Exception as e:
                    print("Error:", e)

# It creates the client session, initializes the agent, and starts the conversation loop.
if __name__ == "__main__":
    asyncio.run(main())