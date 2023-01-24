# Adapted from https://github.com/docker/awesome-compose/blob/master/flask/app/Dockerfile
# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000/udp
EXPOSE 8000/tcp

ENTRYPOINT ["python3"]
CMD ["app.py"]

