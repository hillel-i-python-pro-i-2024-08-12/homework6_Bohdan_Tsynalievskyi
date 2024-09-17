# Homework6_BohdanTsynalievskyi
This project generates a list of humans, each with a name and group association, and organizes this data into a readable format. The output displays the names and number of members in each group. The project uses the `Faker` library to generate random human names and group names, with logic to assign members to random groups and print the organized results.

## Installation
If poetry is not installed please run the following command in the powershell
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Or the following command in Linux
```
curl -sSL https://install.python-poetry.org | python3 -
```
After cloning the repository you can use the following command to initialize virtual environment
```
poetry shell
```

Then you can run the following command to install project dependencies
```
poetry install
```

## Running with poetry
To run the project using poetry please use the following command
```
poetry run python main.py
```
## Running with docker
To run the project using docker please use the following command
```
make d-homework-i-run
```
To purge all data related with services
```
make d-homework-i-purge
```

## Linting
To setup the hooks for linting input:

```
pre-commit install
```

To manually run pre-commit hooks input:
```
poetry run pre-commit run --all-files
```
