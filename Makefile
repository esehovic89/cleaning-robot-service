init:
	echo "Initializing virtual environment in .venv"
	if [ ! -d ".venv" ]; then python -m venv .venv; fi
	echo "Installing dev-requirements"
	source .venv/bin/activate; pip install -r requirements-dev.txt
	echo "Installing pre-commit"
	source .venv/bin/activate; pre-commit install

test:
	docker compose -f docker-compose-test.yml up -d
	pytest
	docker compose -f docker-compose-test.yml down

compile-dependencies:
	@source .venv/bin/activate
	@pip-compile --allow-unsafe --no-emit-index-url requirements.in
	@pip-compile --allow-unsafe --no-emit-index-url requirements-dev.in
