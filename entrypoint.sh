#!/bin/sh
set -e

# Run migrations
python manage.py migrate

# Collect static files
# python manage.py collectstatic --noinput

# Start server
exec python manage.py runserver 0.0.0.0:8080
