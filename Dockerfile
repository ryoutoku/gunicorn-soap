# syntax=docker/dockerfile:1.4

ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

WORKDIR /app
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pip install --no-cache-dir pipenv==2022.1.8 && \
    pipenv sync --dev --system

COPY ./src ./src

ENTRYPOINT [ "gunicorn", "src.wsgi:app" ]