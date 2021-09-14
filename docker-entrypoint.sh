#!/bin/bash
set -e
python manage.py migrate
python manage.py bootstrap
python manage.py runserver 0.0.0.0:8000