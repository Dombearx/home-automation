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
	ssh 192.168.0.201 "rm -rf /home/domin/images/homeariusz.tar"
	scp ./images/homeariusz.tar domin@192.168.0.201:/home/domin/images
	ssh 192.168.0.201 "cd /home/domin/home-assistant; docker-compose stop"
	ssh 192.168.0.201 "cd /home/domin/home-assistant; docker-compose down"
	ssh 192.168.0.201 "docker load -i /home/domin/images/homeariusz.tar"
	ssh 192.168.0.201 "docker image prune -f"
	ssh 192.168.0.201 "docker system prune -f"
	ssh 192.168.0.201 "cd /home/domin/home-assistant; docker-compose up -d"

deploy: docker_build docker_save manage_remote

