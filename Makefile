down:
	docker-compose -f docker-compose.yml down

up:
	docker-compose -f docker-compose.yml up -d

rebuild: down up

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade base

revision:
	alembic revision --autogenerate -m"$(msg)"
