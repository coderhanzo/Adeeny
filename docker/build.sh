#!/bin/sh

# Wait for the database to be ready
./wait-for-it.sh mysql-db:3306 --timeout=30 --strict -- echo "MySQL is up and running!"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Django server
echo "Starting the server..."
exec "$@"
