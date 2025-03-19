from mcp.server.fastmcp import FastMCP

server = FastMCP("Prime Number Checker")

@server.resource("prime://{n}")
def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    server.run(transport="stdio")

if __name__ == "__main__":
    print("Starting server")
    main()