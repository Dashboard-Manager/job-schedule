#!/bin/bash

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
# celery beat
# schedule and execute tasks at intervals
celery -A config.celery beat -l INFO
