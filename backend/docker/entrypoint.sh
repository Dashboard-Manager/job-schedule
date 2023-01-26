#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

# if [ -z "${POSTGRES_USER}" ]; then
#     base_postgres_image_default_user='postgres'
#     export POSTGRES_USER="${base_postgres_image_default_user}"
# fi
# export DATABASE_URL="postgres://$$POSTGRES_USER:$$POSTGRES_PASSWORD@$$POSTGRES_HOST:$$POSTGRES_PORT/$$POSTGRES_DB"

echo "Waiting for postgres database.."
python manage.py check --database default > /dev/null 2> /dev/null
until [ $? -eq 0 ];
do
    sleep 2

python - << 'END_SCRIPT'

    import sys
    import psycopg2
    import environ
    env = environ.Env()

    try:
        conn = psycopg2.connect(
            database=env("POSTGRES_DB"),
            user=env("POSTGRES_USER"),
            password=env("POSTGRES_PASSWORD"),
            host=env("POSTGRES_HOST"),
            port=env("POSTGRES_PORT"),
        )
        print(f"connecting to database ${conn.database}")
    except psycopg2.OperationalError as error:
        print(f"Error connecting to PostgreSQL", error)

    exit()

END_SCRIPT

    python manage.py check --database default > /dev/null 2> /dev/null
    done
    echo "Connected to database."

exec "$@"