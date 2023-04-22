PYTHON=python3

.PHONY: build
build:
	@docker-compose -f docker-compose.yml up --build --force-recreate

.PHONY: up
up:
	@docker-compose -f docker-compose.yml up
