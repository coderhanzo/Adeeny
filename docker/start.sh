#!/bin/sh

set -o errexit

set -o pipefail

set -o nounset

# Wait for the database to be ready
./wait-for-it.sh mysql-db:3306 --timeout=30 --strict -- echo "MySQL is up and running!"

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
# python3 manage.py runserver 0.0.0.0:8000
./wait-for-it.sh mysql-db:3306 -- gunicorn config.wsgi:application --bind 0.0.0.0:8000