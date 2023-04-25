#!/bin/bash

cd /app/lugares_seguros

python manage.py migrate

exec "$@"
