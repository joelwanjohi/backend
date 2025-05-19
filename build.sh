#!/bin/bash

# Exit on error
set -o errexit

# Create necessary directories if they don't exist
mkdir -p staticfiles
mkdir -p media

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create superuser if DJANGO_SUPERUSER_USERNAME is set
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]
then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput || echo "Superuser may already exist."
fi

echo "Build script completed successfully!"