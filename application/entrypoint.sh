#!/bin/sh
poetry run python manage.py makemigrations --noinput
poetry run python manage.py migrate --noinput
poetry run python manage.py collectstatic --noinput
# 環境変数のDEBUGの値がTrueの時はrunserverを、Falseの時はgunicornを実行します
if [$DEBUG == True]; then
    poetry run python manage.py runserver 0.0.0.0:8000
else
    poetry run uwsgi --http 0.0.0.0:8000 --wsgi-file /code/application/wsgi.py
fi