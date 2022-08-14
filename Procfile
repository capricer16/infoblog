web: gunicorn ccva.config.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

