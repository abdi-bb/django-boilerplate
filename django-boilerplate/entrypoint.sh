#!/bin/sh

# Check if DEBUG is set to False (production environment)
if [ -n "$DEBUG" ] && [ "$DEBUG" != "True" ]; then
    echo 'Waiting for postgres...'

    while ! nc -z $DB_HOSTNAME $DB_PORT; do
        sleep 0.1
    done

    echo 'PostgreSQL started'
fi

echo 'Making migrations...'
python manage.py makemigrations

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input

exec "$@"