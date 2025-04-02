# MCP Experiments

This repository contains experiments with MCP (Message Control Protocol) integrated with LangChain and various LLM models.

## Overview
The project demonstrates how to create and use MCP servers with different LLMs (OpenAI and Ollama) with LangChain

## Components

### Servers
- `math_server.py`: A simple MCP server that provides basic math operations (add, multiply)
- `prompts_server.py`: An MCP server handling code review and error debugging prompts
- `weather_server.py`: (Referenced but not shown in context)

### Clients
- `langchain_single_server_client.py`: Connects to a single MCP server using OpenAI's GPT-3.5
- `ollama_langchain_single_server_client.py`: Similar to above but uses Ollama's local LLM
- `langchain_multi_server_client.py`: (Referenced in Makefile but not shown in context)

## Setup

### Prerequisites: 
- Python3+ 
- To run some of the examples you will need an Open AI API key.
    - If you have an OpenAI account, create an API key and store it in a `.env` file. An example `.env` file is provided in the `.env.example` file
- If you do not have an OpenAI account, no worries. There's an example that uses Ollama and llama3.1 
- Install setup a virtual environment and activate it: `make setup` 
 
- You should be able to run any server or clients using the make commands in the Makefile