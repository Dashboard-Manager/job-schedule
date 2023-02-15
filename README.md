 <!-- markdownlint-disable MD033 MD022 MD001 MD041 -->
| Apps | Results |
| ----------- | ----------- |
| pre-commit | [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Dashboard-Manager/job-schedule/main.svg)](https://results.pre-commit.ci/latest/github/Dashboard-Manager/job-schedule/main) |
| coverage | [![Coverage Status](https://coveralls.io/repos/github/Dashboard-Manager/job-schedule/badge.svg?branch=main)](https://coveralls.io/github/Dashboard-Manager/job-schedule?branch=main) |

# Job-schedule
The project presents interactiv dashboard for managing the enterprise, employees, budget and statistics.

### Needed to install
| Program | Version | Links |
| ----------- | ----------- | ----------- |
| Python | 3.11.1 | [link](https://www.python.org/downloads/) |
| Docker | 20.10.22 | [link](https://docs.docker.com/compose/install/) |
| Pipenv | 2022.12.19 | [link](https://pypi.org/project/pipenv/#installation) |
| PostgreSQL | 15.1 | [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) |
| DBeaver | 22.3.4 | [link](https://dbeaver.io/download)
### Clone the project

```bash
  git clone https://github.com/kwiats/job-schedule job-schedule
```

## Local

To your connection in Dbeaver or other you use:

```yaml
  Host: localhost
  Port: 5433
  Database: job-schedule
  Username: job-schedule
  Password: django-app
```

Build database and run connections

```bash
  docker-compose up db --build
```

To navigate if database is builded

```bash
  #to start
  docker-compose start db
  #to stop
  docker-compose stop db
```

### Now run your django application locally when database is started

```bash
  cd job-schedule/backend
```

Install dependencies

```bash
  pipenv install --system
```

Create virtual environment

```bash
  pipenv shell
```

Start the server

```bash
  pipenv run python manage.py runserver_plus
```

Go to site:

```bash
  http://127.0.0.1:8000
```

## Deployment

```bash
  cd job-schedule
```

Run docker

```bash
  docker-compose up --build -d
```

Go to site:

```bash
  http://127.0.0.1:8000
```

## for Develop
### Install packages

```bash
  cd backend
  pipenv install [package]
  #or for dev
  pipenv install [package] --dev
```

### run local develop script

```bash
  cd backend
  ./dev_valid.sh
```

### run test docker script

```bash
  #build test script
  docker-compose -f docker-compose.tests.yml up --build
  #or use only docker-compose up
  docker-compose -f docker-compose.tests.yml up
  #run coverage html result
  start ./htmlcov/index.html

```
