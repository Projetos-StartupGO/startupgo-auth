FROM python:latest

WORKDIR /app
RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system

ADD . /app

RUN DATABASE_URL='sqlite:///db.sqlite' mkdir -p static && python manage.py collectstatic --noinput


ENV UWSGI_WSGI_FILE=/app/project/wsgi.py
ENV UWSGI_HTTP=0.0.0.0:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4
ENV UWSGI_STATIC_MAP="/static/=/app/static/"
CMD [ "uwsgi" ]