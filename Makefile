init:
	@echo "Initializing virtual environment in .venv"
	@if [ ! -d ".venv" ]; then python -m venv .venv; fi
	@echo "Installing dev-requirements"
	@. .venv/bin/activate; pip install -r requirements-dev.txt
	@echo "Installing pre-commit"
	@. .venv/bin/activate; pre-commit install

run:
	python -m uvicorn src.api.main:app --host 0.0.0.0 --port 5000 --reload

test:
	docker compose -f docker-compose-local-db.yml up -d
	pytest
	docker compose -f docker-compose-local-db.yml down

compile-dependencies:
	@. .venv/bin/activate
	@pip-compile --allow-unsafe --no-emit-index-url requirements.in
	@pip-compile --allow-unsafe --no-emit-index-url requirements-dev.in
