install:
	pip install -r requirements.txt

run-client:
	python simple_client_server/clients/langchain_multi_server_mcp_client.py

run-server:
	python simple_client_server/mcp/weather_server.py