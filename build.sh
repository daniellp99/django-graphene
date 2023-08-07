#!/usr/bin/env bash
# exit on error
set -o errexit

poetry config installer.max-workers 10
poetry install --no-interaction --no-ansi -vvv

python manage.py collectstatic --no-input
python manage.py migrate