test:
	@docker compose -f docker-compose-local-db.yml up -d
	@sleep 1
	@pytest
	@docker compose -f docker-compose-local-db.yml down

compile-dependencies:
	@. .venv/bin/activate
	@pip-compile --allow-unsafe --no-emit-index-url requirements.in
	@pip-compile --allow-unsafe --no-emit-index-url requirements-dev.in
