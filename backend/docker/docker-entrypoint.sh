#!/bin/bash

echo "Waiting for postgres database.."
python manage.py check --database default > /dev/null 2> /dev/null
until [ $? -eq 0 ];
do
  sleep 2
  python manage.py check --database default > /dev/null 2> /dev/null
done
echo "Connected to database."

python manage.py makemigrations
python manage.py migrate

exec "$@"
