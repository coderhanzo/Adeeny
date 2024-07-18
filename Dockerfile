# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim as base

# Use an official Python runtime as a parent image

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    pkg-config gdal proj \
    && apt-get clean

# Copy only the pyproject.toml and poetry.lock files to leverage Docker cache
COPY pyproject.toml poetry.lock /usr/src/app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code
COPY ./build.sh /usr/src/app/build.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/build.sh"]

# # Switch to the non-privileged user to run the application.
# USER appuser

# # Expose the port Gunicorn will run on
# EXPOSE 8000

# # Command to run Gunicorn
# CMD ["gunicorn", "config.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
