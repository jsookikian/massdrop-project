#!/usr/bin/env bash
celery -A server.celery worker
python3 server.py