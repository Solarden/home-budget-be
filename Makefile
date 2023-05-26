PYTHON=python3

.PHONY: build
build:
	@docker-compose -f docker-compose.yml up --build --force-recreate

.PHONY: up
up:
	@docker-compose -f docker-compose.yml up

.PHONY: db-migrate
db-migrate:
	@docker exec -it home-budget-backend alembic -c alembic.ini revision --autogenerate

.PHONY: db-upgrade
db-upgrade:
	@docker exec -it home-budget-backend alembic -c alembic.ini  upgrade head

.PHONY: db-downgrade
db-downgrade:
	@docker exec -it home-budget-backend alembic -c alembic.ini  downgrade -1
