ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR $APP_HOME

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
    libmagic1 \
    proj-bin \
    proj-data \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $APP_HOME

RUN pip3 install --upgrade pip && pip3 install wheel && pip3 install poetry && pip3 install mysqlclient

COPY pyproject.toml poetry.lock ./

# Install Poetry environment
RUN poetry config virtualenvs.create false && poetry install && rm -rf $POETRY_CACHE_DIR

COPY ./docker/entry.sh /entry.sh
RUN sed -i 's/\r$//g' /entry.sh
RUN chmod +x /entry.sh

COPY ./docker/build.sh /build.sh
RUN sed -i 's/\r$//g' /build.sh
RUN chmod +x /build.sh

COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn --workers 3 --bind 0.0.0.0:8000 config.wsgi:application"]
# CMD ["/build"]
