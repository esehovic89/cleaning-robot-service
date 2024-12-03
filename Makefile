test:
	docker compose -f docker-compose-test.yml up -d
	pytest
	docker compose -f docker-compose-test.yml down
