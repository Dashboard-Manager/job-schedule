#!/bin/bash

set -o errexit
set -o nounset

# celery worker
# perform tasks from the queue in reality
watchfiles \
    celery.__main__.main --args '-A config.celery worker -l INFO'
