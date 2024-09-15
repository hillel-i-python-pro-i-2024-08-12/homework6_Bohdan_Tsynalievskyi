SHELL := /bin/bash

d-homework-i-run: venv
	source venv/bin/activate && pip install -r requirements.txt && python3 main.py

venv:
	apt update
	apt install -y python3-pip python3.12-venv
	python3 -m venv venv

d-homework-i-purge:
	@echo Goodbye
