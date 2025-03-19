from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# Store active clients for SSE responses
active_clients = set()

@app.post("/mcp")
async def handle_mcp_request(request: Request):
    """
    Handles incoming JSON-RPC 2.0 requests via HTTP.
    """
    data = await request.json()
    
    # Validate JSON-RPC format
    if not isinstance(data, dict) or "jsonrpc" not in data or "method" not in data:
        return JSONResponse({"error": "Invalid JSON-RPC request"}, status_code=400)

    response = {
        "jsonrpc": "2.0",
        "id": data.get("id"),
        "result": f"Echo: {data['method']} with params {data.get('params', {})}"
    }
    
    return JSONResponse(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
