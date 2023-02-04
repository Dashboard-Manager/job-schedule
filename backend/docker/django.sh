#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo "Making migrations for apps [users, earnings, schedules...]"
python manage.py makemigrations users earnings schedules

echo "Apply database migrations"
python manage.py migrate

echo "Running server on 0.0.0.0:8000"
python manage.py runserver_plus 0.0.0.0:8000 --settings=config.settings.dev

exec "$@"

