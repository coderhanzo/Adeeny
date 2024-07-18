#!/usr/bin/env bash
# EXIT ON ERROR

set -o errexit

# install dependencies
poetry install 

# activate virtual environment
poetry shell

# collect static files
python manage.py collectstatic --noinput

# migrated the database
echo "Apply database migrations"

python manage.py migrate

