#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running collectstatic..."
python manage.py collectstatic --noinput


echo "Running Database migrations"
python manage.py migrate

echo "Build, Database migrations and static collection completed successfully."