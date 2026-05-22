# Creating the MCP Client 

##  LangGraph
  - Although there are multiple ways to build MCP clients—including platforms like Claude Desktop, VS Code agents, or the OpenAI Agents SDK—we’ve selected LangGraph because it provides a programmable, event-driven framework for reasoning, tool usage, and state transitions. Its native support for tool routing, message passing, and memory checkpoints aligns well with MCP’s modular interface, making it a practical and scalable solution for client-side orchestration.

## Setting up the client environment#

### Required packages:
  - mcp: This is the official Python SDK for Model Context Protocol.
  - langgraph: This is used to construct a reactive agent capable of tool invocation.
  - langchain_openai: This adapter package integrates OpenAI models with LangChain.
  - langchain_mcp_adapters: It bridges LangChain’s agent interface with the MCP client tools.
```bash
pip install mcp 
pip install langchain
pip install langgraph
pip install langchain-openai
pip install langchain-mcp-adapters
```

## Designing the client agent#
  - Now that our server is ready and our environment is configured, we can design the client agent that will interact with the tools we built. The role of the client agent is to:
    - Accept natural language queries from the user.
    - Decide which tool (or sequence of tools) to use.
    - Call the MCP server via the stdio interface.
    - Return a structured, helpful response.
  
  - We’ll use LangGraph to define the interaction flow as a graph of nodes. Each node represents a reasoning step, such as generating a response or selecting a tool. OpenAI’s LLM powers the agent, and LangChain’s MCP adapters allow tool integration during runtime.

## Defining server connection parameters#
  - The first step in setting up our client is to define how it will connect to the tool server. The MCP server runs as a local subprocess using standard input/output (stdio) as the transport layer. We define the server’s command and arguments using StdioServerParameters.

## How does the agent choose tools?
- Upon receiving a user prompt, the LLM interprets the query’s intent and selects the most appropriate MCP tool(s) based on tool descriptions and expected parameters. It then constructs a structured call, passes parameters, receives the result, and translates it into a natural-language response. This architecture enables dynamic, context-aware behavior without hardcoded logic.

## Using prompts from the client
  - Now that we’ve exposed a prompt on the server, the client needs to discover available prompts, accept user input, and invoke the selected prompt. MCP makes this easy via built-in client APIs like list_prompts() and get_prompt().

## Why prompts matter 
Prompts introduce flexibility and context awareness to MCP-based assistants. They allow agents to reason, prioritize, or summarize in ways tools cannot. This paves the way for building assistants that are intelligent, explainable, and user-centric.

## Using resources from the client
  - Once a resource is registered on the MCP server, it becomes accessible to the client via the session interface. Unlike tools or prompts, resources are not invoked as part of the agent’s reasoning loop—they must be explicitly retrieved and used by the client. This opens up a range of client-side use cases, such as:
    - Displaying static data like topic suggestions or definitions.
    - Preloading configuration values for dynamic prompts.
    - Building menus or filters from server-provided datasets.

## Why resources matter#
  - Resources add a flexible layer to MCP applications. They allow the client to retrieve static, structured data without triggering logic on the server. This enables intelligent assistants to access domain-specific context, populate UI elements, or enrich their reasoning without hardcoding or overloading the model’s context.
  - With tools, prompts, and now resources in place, your MCP-powered agent is equipped to handle a broad spectrum of natural language tasks with modular, declarative support behind the scenes.

