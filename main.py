from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple calculator server")


@mcp.tool
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    return random.randint(min_val, max_val)


@mcp.resource("info://server")
def server_info() -> str:
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server",
        "tools": ["add", "random_number"],
        "author": "Devansh Khatri"
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
