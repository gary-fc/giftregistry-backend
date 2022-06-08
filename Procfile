release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn gift_registry_backend.wsgi --log-file -