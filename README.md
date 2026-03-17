# Text Analyst Agent

## How to run

git clone <repo-url>
cd text-analyst-agent
uv sync
uv run python main.py

---

## Overview

The Text Analyst Agent is a terminal-based application designed to analyze and explore a given text through conversation.

The agent allows users to load a text file and interact with it by asking questions, requesting summaries, and extracting relevant information.

It is built using LangChain and Ollama, and follows a simple and explainable architecture suitable for exam presentation.

---

## Features

* File-based text input (from a controlled data folder)
* Conversational interaction via terminal
* Structured system prompt (MEEPO-style)
* Conversational memory
* Tool usage for text processing
* Streaming output with tool execution visibility
* Clear and explainable architecture

---

## Project structure

text-analyst-agent/
│
├── main.py          # Entry point (CLI interface)
├── agent.py         # Agent logic (LLM + tools + streaming)
├── memory.py        # Conversation memory
├── tools.py         # Custom tools (text splitting, keyword search)
├── prompts.py       # Structured system prompt
├── config.py        # Configuration and settings
├── .env             # Environment variables (not committed)
│
├── data/            # Folder for input text files
│   └── *.txt
│
└── util/            # Provided utilities (from course)
├── models.py
├── pretty_print.py
└── streaming_utils.py

---

## Installation

### For development

Initialize project:
uv init

Add dependencies:
uv add langchain langchain-ollama langgraph python-dotenv

---

### For users (after cloning)

Install dependencies:
uv sync

This ensures the same environment as the original project.

---

## Environment configuration

Create a `.env` file in the root of the project:

OLLAMA_BASE_URL=
OLLAMA_BEARER_TOKEN=YOUR_TOKEN

Important:

* Each user must provide their own token
* Do not commit the `.env` file

---

## How it works

1. The user selects a text file from the `data/` folder
2. The file is loaded and stored in memory
3. The user can ask multiple questions about the same text
4. The agent uses:

   * conversation history
   * source text
   * tools
5. The response is streamed in real time with visible intermediate steps

---

## System prompt design

The agent uses a structured prompt based on the MEEPO framework:

* Mission: analyze and explain a given text
* Expertise: summarization, extraction, question answering
* Environment: terminal-based interaction
* Process: read → understand → extract → answer
* Output: clear and structured
* Guardrails: no hallucinations, only use provided text

---

## Memory

The agent includes a simple conversation memory:

* Stores recent messages (user + assistant)
* Maintains context across multiple questions
* Uses a sliding window to limit memory size

The source text is always injected into the context to ensure grounded responses.

---

## Tools

The agent uses two simple Python tools:

### split_text

* Splits long text into smaller chunks
* Useful for processing large inputs

### search_keyword

* Searches for sentences containing a keyword
* Returns matching parts of the text

The agent automatically decides when to use tools.

---

## Streaming and tool execution

The agent uses streaming execution:

* Outputs are printed in real time
* Tool calls are visible (e.g. `@tool search_keyword`)
* Improves transparency and debugging

Note: When streaming is enabled, the output is handled directly and not returned as a standard string.

---

## Example usage

### Example 1 — Keyword search

Ask:
find how many times the word "AI" appears

Behavior:

* The agent uses the `search_keyword` tool
* Counts occurrences in the text

Result:
The word "AI" appears 8 times in the document

---

### Example 2 — Structured summary

Ask:
summarize the text and divide it by topics

Behavior:

* The agent uses reasoning + text processing
* May use `split_text`

Result:

* Definition of AI
* Applications in industries
* Challenges and ethical concerns
* Future outlook

---

## Commands

* reset → clears conversation memory (keeps loaded text)
* exit → exits the program

---

## Limitations

* Works only with text provided by the user
* No external knowledge retrieval (no RAG)
* Tool behavior depends on model reasoning
* Limited memory window

---

## Performed by

Alessandro Abbate
