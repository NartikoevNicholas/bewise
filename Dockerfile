FROM python:3.11-alpine3.18

RUN pip install poetry
RUN apk update

WORKDIR /app
COPY . /app/

RUN poetry install
CMD poetry run alembic upgrade head && poetry run uvicorn app.main:app --host=0.0.0.0 --port=8080
