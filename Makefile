black:
	black ./src

flake:
	autoflake --quiet --in-place --recursive --ignore-init-module-imports --remove-unused-variables --remove-all-unused-imports ./src

isort:
	isort ./src

typehint_check:
	mypy --no-site-packages --ignore-missing-imports --no-strict-optional ./src

format: flake black isort typehint_check

requirements:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt
