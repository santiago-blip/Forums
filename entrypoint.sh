#!/bin/bash

#VALIDATE DB
# ./wait-for-postgres.sh db_postgres

#RUN PROJECT
#VALIDATE IF A FOLDER ALREADY EXISTS
# [ ! -d /app/forumCore ] && django-admin startproject forumCore .

#run migrations
echo "Running makemigrations..."
python manage.py makemigrations
echo "Running migrate..."
python manage.py migrate

python manage.py runserver 0.0.0.0:8000