#!/bin/bash

set -o errexit
set -o nounset

# until timeout 5s celery -A config.celery inspect ping; do
#     echo >&2 "Celery workers not available"
# done

echo "========== CELERY FLOWER ON =========="
# Flowers
# graphical interface for celery workers
sleep 5
celery \
    -A config.celery \
    -b "${CELERY_BROKER_URL}" \
    flower \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
