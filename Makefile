#!make
SHELL:=/bin/bash
include .envs/.django
include .envs/.postgres


start:
	docker-compose up -d
	sleep 10
	docker exec -ti krivov_local_django sh -c "python manage.py loaddata --format=json fixtures/init.json"
	echo "USER: root PASSWORD: q1w2e3w2e3"

clear:
	docker-compose down --rmi all
