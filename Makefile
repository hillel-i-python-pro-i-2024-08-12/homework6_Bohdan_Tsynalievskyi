.PHONY: d-homework-i-run d-homework-i-purge lint

SHELL := /bin/bash

d-homework-i-run:
	@echo "Running homework in Docker"
	docker compose up --build

d-homework-i-purge:
	@echo "Purging Docker containers and images"
	docker compose down --rmi all --volumes --remove-orphans

lint:
	poetry run isort .
	poetry run black .
	poetry run flake8 .
