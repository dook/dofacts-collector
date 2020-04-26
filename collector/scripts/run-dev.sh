#! /usr/bin/env sh
set -e

python /app/scripts/db_migrate.py
exec uvicorn --reload --host $COLLECTOR_HOST --port $COLLECTOR_PORT --log-level $COLLECTOR_LOG_LEVEL "collector.app:app"