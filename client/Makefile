black:
	poetry run black .

flake:
	poetry run autoflake --quiet --in-place --recursive --ignore-init-module-imports --remove-unused-variables --remove-all-unused-imports .

isort:
	poetry run isort .

typehint_check:
	poetry run mypy --no-site-packages --ignore-missing-imports --no-strict-optional --explicit-package-bases .

format: flake typehint_check black

install:
	poetry install --no-root

run:
	poetry run python ./main.py

run_server:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8001 --reload