FROM python:3.10.0-slim-bullseye
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

RUN apt-get update && apt-get install -y build-essential zlib1g-dev libjpeg-dev libpq-dev && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

RUN python manage.py collectstatic --noinput
CMD gunicorn --worker-tmp-dir /dev/shm -w 2 --log-file=- -b :8000 project.wsgi:application
