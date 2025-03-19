# Simple MCP server with stdio

### Register the client 
```
{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"tinyclient","version":"1.0"}},"id":1}
```

### Send a request to the server 
```
{"jsonrpc": "2.0","method":"resources/read","params": {"uri":"prime://17"},"id": 2}
```