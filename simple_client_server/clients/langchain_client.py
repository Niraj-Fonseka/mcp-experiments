from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo")
import asyncio  


async def run_agent():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["simple_client_server/mcp/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
             "time": {
                # make sure you start your weather server on port 8000
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["-m", "mcp_server_time", "--local-timezone=America/Chicago"],
                "transport": "stdio",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        #response = await agent.ainvoke({"messages": "what's (3 + 5) x 12? and what is the weather in nyc?"})
        response = await agent.ainvoke({"messages": "What is the time now ?"})
        #print(response)
        #weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
        print(get_final_answer(response))

def get_final_answer(response):
    return response['messages'][len(response['messages']) - 1].content

if __name__ == "__main__":
    asyncio.run(run_agent())