import multiprocessing
import os

cores = multiprocessing.cpu_count()
workers_per_core = int(os.getenv("WORKERS_PER_CORE", "1"))
default_web_concurrency = workers_per_core * cores
web_concurrency = int(os.getenv("WEB_CONCURRENCY", 0))
host = os.getenv("COLLECTOR_HOST", "0.0.0.0")
port = os.getenv("COLLECTOR_PORT", "80")

# Gunicorn config variables
loglevel = os.getenv("COLLECTOR_LOG_LEVEL", "info")
workers = max(web_concurrency, default_web_concurrency)
bind = f"{host}:{port}"
keepalive = 120
errorlog = "-"
