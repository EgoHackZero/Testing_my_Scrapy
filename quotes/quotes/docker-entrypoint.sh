#!/bin/sh

pythoт manage.py db migrate
python manage.py runserver 0.0.0.0:8080