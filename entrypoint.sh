#!/bin/sh

# Optional: Wait for the database to be ready
# This assumes your database service is named 'db' and runs on port 5432
# Adjust 'db' and '5432' if your database hostname or port is different
echo "Waiting for PostgreSQL..."
# Using pg_isready from postgresql-client

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo "PostgreSQL is ready!"

# Run Alembic migrations
echo "Running Alembic migrations..."
poetry run alembic upgrade head
echo "Alembic migrations completed."

# Execute the main command passed to CMD (or any arguments passed to docker run)
exec "$@"