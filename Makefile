POSGRES_USER = root
DB_NAME = test

env:
	cp .env.example .env

app_run:
	poetry run uvicorn app.main:app

docker_run:
	make env
	docker-compose -f docker-compose.yml up -d --remove-orphans

docker_open_psql:
	docker exec -it backend_postgres psql -U $(POSGRES_USER) -d $(DB_NAME)

docker_clear:
	docker rm -f `docker ps -qa`
	docker rmi -f `docker images -qa`
	docker volume prune -a
	docker system prune --volumes
	docker network prune -a