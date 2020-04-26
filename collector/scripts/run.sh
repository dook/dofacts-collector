#! /usr/bin/env sh
set -e

exec gunicorn -k uvicorn.workers.UvicornWorker -c "/app/gunicorn.conf.py" "collector.app:app"