black:
	poetry run black ./src

flake:
	poetry run autoflake --quiet --in-place --recursive --ignore-init-module-imports --remove-unused-variables --remove-all-unused-imports ./src

isort:
	poetry run isort ./src

typehint_check:
	poetry run mypy --no-site-packages --ignore-missing-imports --no-strict-optional ./src

format: flake black isort typehint_check

install:
	poetry install
