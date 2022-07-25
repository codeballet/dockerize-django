# Dockerize Django

## Introduction

Dockerize Django is an example of how Django may be run under Docker. The Django app here is a simple note taking app.

The app is by default using the sqlite database. However, you may enable the Postgres option in the `docker-compose.yml` file, and appropriately change the code in the app if you want to use Postgres instead. See the below section "Connecting to a Postgres database" for more information.

Using the approach in this project, neither Python, pip, nor Django is necessary to install locally on the computer. Django is not running directly on your computer, but inside of Docker. All that is necessary is Docker. The `docker-compose.yml` file will use `volumes` to create a copy of the Django project in your local directory, where your `docker-compose.yml` file is stored. Any changes you do in that directory will be reflected in the Django app that is running in a Docker container.

## Requirements

Docker.

## How to use

The repository contains a full web app, however, if you want to create your own Django project and apps, you may simply use the `Dockerfile`, the `docker-compose.yml`, and the `requirements.txt` files to create your own projects and apps.

### Create a new Django project:

If you want to create a new project, in this example named "composeexample", run the command (do not forget the dot at the end):

```
sudo docker-compose run web django-admin startproject composeexample .
```

If you are running Docker on Linux, the files django-admin created are owned by the `root` user. This happens because the container runs as the `root` user. Change the ownership of the new files created by docker in your local directory with the command:

```
sudo chown -R $USER:$USER composeexample manage.py
```

In case you enable the Postgres option, do not change the permission of the data folder where Postgres has its file, otherwise Postgres will not be able to start due to permission issues.

### Connecting to a Postgres database (optional, by default disabled in `docker-compose.yml`)

In your project directory, edit the `composeexample/settings.py` file.

Replace the DATABASES = ... with the following:

```
import os

[...]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

These settings are determined by the postgres Docker image specified in docker-compose.yml.

### Run a test with the Django development server

You should now be able to run the default Django app on URL `http://localhost:8000` with the command:

```
docker-compose up
```

### Shutting down the Django development server

Either run

```
docker-compose down
```

in a new terminal window, under the directory where you have your `docker-compose.yml` file.

ALternatively, press `Ctrl+C`.

### Create a new app

To create a new app, which in the case of this project is named "tasks", run:

```
sudo docker-compose run web python manage.py startapp tasks
```

As in the case of creating a project, Docker on Linux by default creates files and folders owned by the `root` user. Change the ownership of the newly created `tasks` directory with:

```
sudo chown -R $USER:$USER tasks
```

### Migration

Run command:

```
docker-compose run web python manage.py migrate
```

## Acknowledgements

The project is an adaption of the official Docker documentation, which you can read [here](https://docs.docker.com/samples/django/)
