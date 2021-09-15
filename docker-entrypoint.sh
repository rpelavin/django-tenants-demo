#!/bin/bash
set -e
python manage.py migrate_schemas
python manage.py migrate_schemas --shared
python manage.py bootstrap \
    --admin-username $ADMIN_USERNAME \
    --admin-email $ADMIN_EMAIL \
    --admin-password $ADMIN_PASSWORD
python manage.py runserver 0.0.0.0:8000