#!/bin/bash
set -e
python manage.py migrate_schemas
python manage.py migrate_schemas --shared
python manage.py bootstrap
python manage.py runserver 0.0.0.0:8000