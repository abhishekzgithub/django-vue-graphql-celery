celery -A productimporter worker -l info -P eventlet
celery -A productimporter beat -l info

python manage.py runserver
