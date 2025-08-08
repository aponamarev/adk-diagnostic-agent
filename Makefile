# Makefile for managing the diagnostic agent Docker environment

# Variables
DOCKER_COMPOSE_FILE := ./docker-compose.yml
.PHONY: build web console stop reset

# Build the Docker images
build:
	docker compose -f $(DOCKER_COMPOSE_FILE) build --no-cache

# Run the web UI for the diagnostic agent
web:
	docker compose -f $(DOCKER_COMPOSE_FILE) up

# Run the diagnostic agent in interactive console mode
console:
	docker compose -f $(DOCKER_COMPOSE_FILE) run --rm diagnostic_agent pdm run adk run src/diagnostic_agent

# Stop and remove the running containers
stop:
	docker compose -f $(DOCKER_COMPOSE_FILE) down --remove-orphans --volumes

# Reset the database
reset:
	docker compose -f $(DOCKER_COMPOSE_FILE) down --remove-orphans --volumes --rmi all
	docker compose -f $(DOCKER_COMPOSE_FILE) build --no-cache

