.PHONY: help delivery_service build-nc up down shell migration-autogenerate migration-upgrade


include .env.make
export ENV_FILE

GID := $(shell id -g)
UID := $(shell id -u)

help: ## Show help for each of the Makefile recipes.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build an application docker image.
	@docker build -f $(DOCKERFILE) -t delivery-service --build-arg GID=$(GID) --build-arg UID=$(UID) ../

build-nc: ## Build an application docker image without using cache.
	@docker build --no-cache -f $(DOCKERFILE) -t delivery-service ../

up: ## Starts the application.
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) up -d

logs: ## Shows logs of the delivery service.
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) logs -f app

down: ## Stops and removes application containers.
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) down

shell: ## Connects to the container shell.
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) exec -it app sh

migration-autogenerate: ## Generates the alembic migration file.
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) run --rm app-migration bash -c 'cd /migrations && alembic revision --autogenerate'

migration-upgrade: ## Runs migration files.
	@docker compose -f $(COMPOSE_FILE) --env-file $(ENV_FILE) run --rm app-migration bash -c 'cd /migrations && alembic upgrade head'
