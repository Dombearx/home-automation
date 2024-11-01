black:
	poetry run black ./src

flake:
	poetry run autoflake --quiet --in-place --recursive --ignore-init-module-imports --remove-unused-variables --remove-all-unused-imports ./src

isort:
	poetry run isort ./src

typehint_check:
	poetry run mypy --no-site-packages --ignore-missing-imports --no-strict-optional --explicit-package-bases ./src

format: flake typehint_check black

install:
	poetry install --no-root

run:
	poetry run python ./main.py

docker_build:
	docker system prune -f
	docker build -t homeariusz .
	docker image prune -f

docker_save:
	rm -rf ./images/homeariusz.tar
	docker save -o ./images/homeariusz.tar homeariusz

manage_remote:
	ssh 192.168.0.201 "rm -rf ./images/homeariusz.tar"
	scp ./images/homeariusz.tar domin@192.168.0.201:/home/domin/images
	ssh 192.168.0.201 "cd /home/domin/home-assistant; docker-compose stop"
	ssh 192.168.0.201 "cd /home/domin/home-assistant; docker-compose down"
	ssh 192.168.0.201 "docker load -i /home/domin/images/homeariusz.tar"
	ssh 192.168.0.201 "docker image prune -f"
	ssh 192.168.0.201 "docker system prune -f"
	ssh 192.168.0.201 "cd /home/domin/home-assistant; docker-compose up -d"

deploy: docker_build docker_save manage_remote

.PHONY: update-dependencies
update-dependencies:
	@dependencies=$$(awk '/\[tool.poetry.dependencies\]/ {flag=1; next} /^\[/{flag=0} flag && /^[[:space:]]*[a-zA-Z0-9_-]+[[:space:]]*=/ {print $$1}' pyproject.toml); \
	installed_packages=$$(poetry show -l); \
	for dependency in $$dependencies; do \
		if [ "$$dependency" != "python" ]; then \
			current_version=$$(echo "$$installed_packages" | grep -A 0 "^$$dependency " | awk '{print $$2}'); \
			latest_version=$$(echo "$$installed_packages" | grep -A 0 "^$$dependency " | awk '{print $$3}'); \
			if [ "$$current_version" != "$$latest_version" ]; then \
				echo "Updating $$dependency from $$current_version to $$latest_version"; \
				poetry add "$$dependency@latest"; \
			else \
				echo "$$dependency is already up-to-date"; \
			fi; \
		fi; \
	done