 <!-- markdownlint-disable MD033 MD022 MD001 MD041 -->

| Apps       | Results                                                                                                                                                                                        |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pre-commit | [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Dashboard-Manager/job-schedule/main.svg)](https://results.pre-commit.ci/latest/github/Dashboard-Manager/job-schedule/main) |
| coverage   | [![Coverage Status](https://coveralls.io/repos/github/Dashboard-Manager/job-schedule/badge.svg?branch=main)](https://coveralls.io/github/Dashboard-Manager/job-schedule?branch=main)           |

# Job-schedule

The project presents interactiv dashboard for managing the enterprise, employees, budget and statistics.

### Needed to install

| Program    | Version  | Links                                                                        |
| ---------- | -------- | ---------------------------------------------------------------------------- |
| Python     | 3.11.1   | [link](https://www.python.org/downloads/)                                    |
| Docker     | 20.10.22 | [link](https://docs.docker.com/compose/install/)                             |
| Poetry     | 1.3.2    | [link](https://python-poetry.org/docs/#installation)                         |
| Node.js    | 9.5.21   | [link](https://nodejs.org/en/)                                               |
| PostgreSQL | 15.1     | [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) |
| DBeaver    | 22.3.4   | [link](https://dbeaver.io/download)                                          |

### Clone the project

```bash
  git clone https://github.com/kwiats/job-schedule job-schedule
```

### Run project

```bash
  docker-compose up --build
```

# Local

If you need install some new dependencies, do it like this:

### Install backend packages

```bash
  # you can use version-number or latest
  cd backend
  poetry install <package-name>@latest
  poetry export --with production --with dev -f requirements.txt --output requirements.txt
```

### Install frontend installation

```bash
  # you can use version-number or latest
  cd frontend
  npm install <package-name>@latest
  npm install # to install all frontend dependencies
```

If you install some new dependencies, again build app.

```bash
  docker-compose up frontend --build # to build only frontend package
  docker-compose up --build # to build full api
```

## Local install only postgres

To your connection in Dbeaver or other you use:

```yaml
Host: localhost
Port: 5433
Database: job-schedule
Username: job-schedule
Password: django-app
```

Build postgres database and run connections

```bash
  docker-compose up postgres --build
```

To navigate if database is builded

```bash
  #to start
  docker-compose start postgres
  #to stop
  docker-compose stop postgres
```

### Backend makemigrations app

```bash
  # remove migration
  rm -rf backend/apps/<app>/migrations/
  # use if django don't stand up
  docker-compose run --rm django sh -c "python manage.py makemigrations <app-name>"
  # use when django is running
  docker-compose exec -it django sh -c "python manage.py makemigrations <app-name>"
  # if you got "No changes detected in app '<app-name>'"
  # and you dont have makemigrations folder in your app
  docker-compose run --rm django sh -c "python manage.py makemigrations --empty <app-name>"
  # if you need you can remove postgres database
  docker volume rm job_schedule_postgres_data
  # remeber you can connect commands like remove migrations and add changes in one step
  rm -rf backend/apps/<app>/migrations/ && docker-compose run --rm django python manage.py makemigrations <app-name>
```

## Deployment

### Run only backend

```bash
  docker-compose up django
```

### Run only frontend

```bash
  docker-compose up frontend
```

# for Develop

## Backend

### Create app in apps

```bash
  # connect container django
  cd backend
  # create new app
  python manage.py startapp <app-name>
  # move app to folder apps in project
  mv <app-name> apps
```

The next you need do some steps with app

```py
  # change apps.py in your app folder
  in apps/<app-name>/apps.py change name to: "apps.<app-name>"
  # add your app to project LOCAL_APPS
  in config/settings.base LOCAL_APPS add "apps.<app-name>"
  # create urls.py in app dir and create empty urlpatterns
  in apps/<app-name> create urls.py with urlpatterns = []
  # in config urls add paths to your app
  in config/urls.py add path("api/<app-name>/", include("apps.<app-name>.urls")),
```

### Run tests and linters after deployment app

```bash
  # checks:pytest, coverage, mypy tests
  # -flake8, isort styles
  docker-compose exec -it django bash -c "docker/debug/run.sh"
```

Run one test only

```bash
  # pytest
  docker-compose exec -it django pytest -s -v --no-migrations
  # coverage
  docker-compose exec -it django pytest --cov=apps --cov=config --cov-config=.coveragerc && coverage html
  # mypy
  docker-compose exec -it django mypy . --config-file mypy.ini
  # flake8
  docker-compose exec -it django flake8 . --config=setup.cfg
  # isort
  docker-compose exec -it django isort . --settings-path=.isort.cfg
```

You can still do this commands inside virtual enviroments like:

```bash
  docker-compose exec -it django bash
```

then you are logged in container as root:

```bash
  root@some_number:/some_path# flake8 . --config=setup.cfg
```

and do this same commands

## Frontend

### Functional tests with cypress and e2e

For functional tests you do:

```bash
  cd frontend
  npm run cypress:open
```

and then chose e2e tests
or

```bash
  cd frontend
  npm run cypress:run
```

### Integration tests

For integration tests, you can use two ways:

1. You can install [vscode-jest](https://github.com/jest-community/vscode-jest#getting-started) and in VS Code press F1 and chose 'Jest Start All Runners or
2. Chose Run and Debug 'Run Jest'
