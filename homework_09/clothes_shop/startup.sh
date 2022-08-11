#!/bin/bash
DJANGO_APPS=("shopapp" "siteauth")
for app in ${DJANGO_APPS[@]}; do
  python manage.py makemigrations $app
done
python manage.py makemigrations
python manage.py migrate

./manage.py test

DJANGO_SUPERUSER_PASSWORD=administrator
export DJANGO_SUPERUSER_PASSWORD
DJANGO_SUPERUSER_EMAIL=administrator@admin.com
DJANGO_SUPERUSER_USERNAME=administrator
if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py runserver 0.0.0.0:8000