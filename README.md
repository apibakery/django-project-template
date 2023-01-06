# Project Template

Empty Django REST Framework project template generated using
https://apibakery.com

Contains just one model, "Hello", to showcase the empty project structure and features:

* OpenAPI / Swagger support
* static file serving using WhiteNoise
* email support using Anymail
* background workers support using Celery
* Django admin
* Docker support
* unit tests
* code formatting using black

This code is open source, licensed under the MIT license (see end of this document).
If you need a different license, create your own template project for free using
https://apibakery.com


## Quickstart

1. Set up a Python virtual environment and install the required Python dependencies:

        python3 -m venv <path-to-virtualenv>
        source <path-to-virtualenv>/bin/activate
        pip install -r requirements.txt

2. Create `.env` configuration file based on `env.sample`:

        cp env.sample .env
        vim .env

3. Set up the database

    You'll need to create the database and set `DATABASE_URL` in
    the configuration file before you can run migrations and use the code.

    To use SQLite (supported out of the box), set the `DATABASE_URL` to
    the location of database file (it will be created on the first run),
    either relative to the project directory:

        DATABASE_URL=sqlite:///sqlite.db

    Or absolutely positioned in the file system:

        DATABASE_URL=sqlite:////full/path/to/sqlite.db

    (Note the three or four dashes in the URL, respectively).

    To use PostgreSQL or MariaDB databases, install the appropriate
    driver and create database and user as needed. Example for
    PostgreSQL (this assumes you already have PostgreSQL installed
    on your system via package manager such as apt, rpm, or brew):

    1. Connect to the database as admin and create a new user and database

        CREATE USER 'appuser' WITH PASSWORD 'secretpassword';
        CREATE DATABASE 'dbname' WITH OWNER 'appuser';

    2. Install Python database driver for PostgreSQL

        pip install psycopg2

    3. Set up `DATABASE_URL` in your `.env`:

        DATABASE_URL=postgres://appuser:secretpassword@localhost/dbname

4. Run migrations:

        python manage.py makemigrations
        python manage.py migrate

4. Run the server:

        python manage.py runserver

5. Visit the browsable API at http://localhost:8000/api/v1/

6. Access the Django admin at http://localhost:8000/admin/

## Creating superuser

A superuser account can be created using the Django management command:

    python manage.py createsuperuser


## Running tests

    python manage.py test


## Code formatting using black

To format the code automatically using `black`,
just run it in the project directory:

    black .

## Background tasks using Celery

Use `CELERY_BROKER_URL` and `CELERY_BACKEND` environment variables to
configure broker and optional results backend to use for the background
jobs, see `env.sample` for details.

Tasks are defined in `tasks.py` in the appropriate app module.

To run the worker, in the project root, run:

        celery -A project worker

Logging from the tasks will be shown/hidden based on the celery worker
log level (default is `WARNING`, can be changed with `-l LEVEL` worker
option), not based on Django logging configuration.

To show `INFO` or higher-priority messages, use:

        celery -A project worker -l INFO

To run periodic tasks using Celery Beat, specify beat entries
in `settings/base.py` and run celery beat:

        celery -A project beat -l INFO

## Docker support

Build the docker image with:

        docker build -t project-template .

The default command is to start the web server (gunicorn). Run the image
with `-P` docker option to expose the internal port and check the exposed
port with `docker ps`:

        docker run --env-file .env --P project-template
        docker ps

Make sure you provide the correct path to the env file (this example assumes
it's located in the local directory).

To run a custom command using the image (for example, db migrations):

        docker run --env-file .env project-template python manage.py migrate

To run a Django shell inside the container:

        docker run --env-file .env -t project-template

Note that any changes inside the container will be lost. For that reason,
running `collectstatic` or using a SQLite database within a container will
have no effect. If you want to use SQLite with docker, mount a docker
volume and place the SQLite database inside it.

For more information on the docker build process, see the included `Dockerfile`.

## License

Copyright 2023 Senko Rasic <senko@apibakery.com>.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
