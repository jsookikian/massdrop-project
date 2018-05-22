#!/usr/bin/env bash

# Amazon EC-2 Instance setup script

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
celery -A server.celery worker
python3 server.py




