# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7
ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim as base

ENV APP_HOME=/app \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache


RUN apt-get update && apt-get install -y \
    gcc \
    binutils \
    libproj-dev \
    gdal-bin \
    pkg-config \
    libpq-dev \
    proj-bin \
    proj-data \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \

WORKDIR $APP_HOME

RUN pip3 install --upgrade pip && pip3 install wheel && pip3 install poetry && pip3 install mysqlclient

COPY pyproject.toml poetry.lock ./

# RUN mkdir $APP_HOME/staticfiles

# Install Poetry environment

RUN poetry config virtualenvs.create false && poetry install && rm -rf $POETRY_CACHE_DIR

COPY ./docker/entry /entry
RUN sed -i 's/\r$//g' /entry
RUN chmod +x /entry

COPY ./docker/build /build
RUN sed -i 's/\r$//g' /build
RUN chmod +x /build


CMD ["/entry"]
