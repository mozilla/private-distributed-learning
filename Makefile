.PHONY: build up down

setup_conda:
	# Install all dependencies and setup repo in dev mode
	conda env update -n pdl -f environment.yml
	python setup.py develop

build:
	docker build . -t app:latest

up:
	docker-compose up

down:
	docker-compose down
	docker-compose stop
