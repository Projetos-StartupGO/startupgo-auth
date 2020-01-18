FROM python:latest

WORKDIR /app
RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system

ADD . /app

CMD [ "uwsgi" ]