setup: setup-venv install

setup-venv:
	python -m venv .venv

.ONESHELL:
install:
	source .venv/bin/activate && pip install -r requirements.txt

.ONESHELL:
run-single-server-client:
	source .venv/bin/activate && python langchain_single_server_client.py

.ONESHELL:
run-multi-server-client:
	source .venv/bin/activate && python langchain_multi_server_client.py

.ONESHELL:
run-weather-server:	
	source .venv/bin/activate && python servers/weather_server.py

.ONESHELL:		
run-math-server:
	source .venv/bin/activate && python servers/math_server.py

clean:
	rm -rf .venv

source:
	source .venv/bin/activate