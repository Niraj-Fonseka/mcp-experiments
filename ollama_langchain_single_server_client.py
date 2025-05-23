# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_ollama import ChatOllama

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

import asyncio  


model = ChatOllama(model="llama3.1")

server_params = StdioServerParameters(
    command="python",
    args=["simple_client_server/mcp/math_server.py"],
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            print(get_final_answer(agent_response))


def get_final_answer(response):
    return response['messages'][len(response['messages']) - 1].content

if __name__ == "__main__":
    asyncio.run(run_agent())