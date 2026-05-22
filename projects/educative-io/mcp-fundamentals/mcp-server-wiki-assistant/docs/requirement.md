# Creating the MCP Server

## Scenario: Wikipedia research assistant
  - Imagine we’re building a knowledge assistant for curious minds—students, journalists, or professionals—who frequently use Wikipedia for background research. Instead of opening tabs and scanning walls of text, users should be able to ask “Tell me about Alan Turing,” or “Summarize the topic of carbon cycles,” and receive structured results: a clean summary, the article title, and a link to the full page.

  - For this purpose, we will use the MCP to communicate with a backend server that understands how to retrieve and package information from Wikipedia. In this lesson, we’ll build that server component of such a system using Python. Let’s begin by preparing the development environment.

## how to do it 
  - Before we implement our server, we need to set up the environment. The following are the required libraries:
    - **wikipedia:** A simple Python wrapper for the Wikipedia API. We’ll use it to search topics, fetch article metadata, and extract content.
    - **mcp:** The official Python SDK for Model Context Protocol. It provides the FastMCP interface that lets us expose tools from our server.
  - We can install these libraries locally using the following commands:
```bash
pip install wikipedia
pip install mcp
```
## Implementing the list_wikipedia_sections tool
In many cases, users don’t just want a summary. They want to explore specific parts of an article. To support this, we need a way to programmatically extract the structure of a Wikipedia page. The list_wikipedia_sections tool will help us do exactly that. It takes a topic as input and returns a list of section titles from the corresponding Wikipedia page. This allows the AI assistant to guide users through the content or offer them options to dive deeper into specific sections.

pip install wikipedia_sections


## Implementing the get_section_content tool
- Now that we can list available sections, let’s see how to extract the actual content from a specific section. For this purpose, we will implement the get_section_content tool, which will fetch the full text of a specific section from a Wikipedia article. This is useful when a user asks to “show me the early life section” or “give me the research contributions part” of an article.

## overall
- By exposing get_section_content as a standalone tool, we make it easy for agents to “compose” multi-step workflows, such as: search → list sections → fetch section content. Because these steps are programmable, an agent can decide which tools to use, in what order, and how to handle errors, showcasing the programmability built into MCP.

## What are the prompts in MCP?
  - In MCP, prompts are predefined text templates that guide the behavior of a language model. Whereas tools are invoked and executed server-side to produce structured outputs, prompts are passive: they return a text string when called. This string typically contains a carefully crafted instruction injected into the LLM’s context.

  - Prompts are particularly useful when:
    - The task requires summarization, prioritization, or natural language reasoning.
    - The assistant should express user intent declaratively rather than procedurally.
  
  - MCP prompts are:
    - Defined and hosted on the server, but not executed there.
    - Discovered and invoked by the client, just like tools.
    - Parameterized so users can pass in structured inputs like topic: str.
    - Deterministic in return value, always returning a text block (not JSON or function output).

# What are the resources in MCP?#
  - Resources in MCP are named, structured data objects exposed by the server but retrieved and used entirely by the client. They’re useful when the assistant needs reference information that doesn’t change frequently and doesn’t require computation, like recommended topics, glossary terms, or API keys.
  - Resources are typically used to:
    - Provide contextual background (e.g., a list of predefined topics).
    - Inject static configuration or preferences.
    - Support client-side filtering, choices, or menus.