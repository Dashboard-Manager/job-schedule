#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

# CREATE ENVIRONMENTS
#CHECKS POSTGRES USER EXISTS if not SET DEFAULT
if [[ -z "${POSTGRES_USER+x}" ]]; then
    export POSTGRES_USER="default_user"
else
    export POSTGRES_USER="${POSTGRES_USER}"
fi

export POSTGRES_DB="${POSTGRES_DB}"
export POSTGRES_PASSWORD="${POSTGRES_PASSWORD}"
export POSTGRES_HOST="${POSTGRES_HOST}"
export POSTGRES_PORT="${POSTGRES_PORT}"
# CREATE REDIS URL
export CELERY_BROKER_URL="${REDIS_URL}"
# CREATE DJANGO DATABASE_URL to POSTGRES
export DATABASE_URL="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"

# RUN POSTGRES SCRIPT
postgres_ready() {
    python <<END
import sys
import time
import psycopg2


class PostgresDB:
    def __init__(self, dbname, user, password, host, port=5432):
        self.config = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port,
        }

    def connect_to_db(self, max_retries=10, retry_delay=1):
        start = time.time()
        retry_count = 0
        while True:
            try:
                psycopg2.connect(**self.config)
                break
            except psycopg2.OperationalError as error:
                retry_count += 1
                sys.stderr.write(f"Waiting for PostgreSQL to become available (retry {retry_count}/{max_retries})...\n")
                if retry_count >= max_retries:
                    sys.stderr.write(f"Maximum number of retries ({max_retries}) reached. Aborting...\n")
                    raise error
                if time.time() - start > suggest_unrecoverable_after:
                    sys.stderr.write("  This is taking longer than expected. The following exception may be indicative of an unrecoverable error: '{}'\n".format(error))
                time.sleep(retry_delay * retry_count)

postgres_config = {
    "dbname": "$POSTGRES_DB",
    "user": "$POSTGRES_USER",
    "password": "$POSTGRES_PASSWORD",
    "host": "$POSTGRES_HOST",
    "port": $POSTGRES_PORT,
}
try:
    db = PostgresDB(**postgres_config)
    db.connect_to_db()
except psycopg2.Error as error:
    print('PostgreSQL is unavailable', error)
END
}
until postgres_ready; do
    echo >&2 'Waiting for PostgreSQL to become available...'
    sleep 1
done
echo >&2 'PostgreSQL is available' $(date '+%H:%M:%S')

exec "$@"
