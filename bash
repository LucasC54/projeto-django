pip install django

django-admin startproject luuhart
cd luuhart

python manage.py startapp core

python manage.py migrate

python manage.py runserver