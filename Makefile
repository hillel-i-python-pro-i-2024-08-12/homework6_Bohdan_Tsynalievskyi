SHELL := /bin/bash

d-homework-i-run: venv
	source venv/bin/activate && pip install --requirement requirements.txt && python3.12 main.py

venv:
	apt update
	apt install --yes software-properties-common
	add-apt-repository ppa:deadsnakes/ppa -y
	apt update
	apt install --yes python3.12 python3.12-venv python3-pip
	python3.12 -m venv venv

d-homework-i-purge:
	@echo Goodbye
