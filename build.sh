#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirimiento.txt
python manage.py collectstatic --no-input
python manage.py migrate