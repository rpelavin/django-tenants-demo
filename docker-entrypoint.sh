#!/bin/bash
set -e
python manage.py migrate_schemas
python manage.py migrate_schemas --shared
python manage.py create_public_tenant \
    --public-tenant-domain $PUBLIC_TENANT_DOMAIN \
    --superuser-username $SUPERUSER_USERNAME \
    --superuser-email $SUPERUSER_EMAIL \
    --superuser-password $SUPERUSER_PASSWORD
python manage.py runserver 0.0.0.0:8000