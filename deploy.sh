#!/usr/bin/env bash
celery -A server.celery worker > /dev/null 2>&1 &
python3 server.py
