#!/bin/bash

cd /api/places

python manage.py migrate

exec "$@"