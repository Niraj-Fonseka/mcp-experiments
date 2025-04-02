from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    if location == "New York":
        return "It's always sunny in New York"
    elif location == "Chicago":
        return "It's cloudy in Chicago"
    elif location == "Los Angeles":
        return "It's sunny in Los Angeles"
    elif location == "San Francisco":
        return "It's foggy in San Francisco"
    else:
        return "I don't know the weather in that location"

if __name__ == "__main__":
    mcp.run(transport="sse")