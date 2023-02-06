 <!-- markdownlint-disable MD033 MD022 MD001 MD041 -->
| Apps | Results |
| ----------- | ----------- |
| pre-commit | [![pre-commit.ci status](https://results.pre-commit.ci/latest/github/Dashboard-Manager/job-schedule/main) |
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

### Setup local PostgreSQL database

<ol>
  <li>Before you start build server you need check some steps and maybe change it:</li>
  <p>find your pg_hba.conf file in your system and change this too look similar this</p>
  <code>local   all             postgres                                peer</code><br>
  <code>host    all       all             0.0.0.0/0             md5</code><br>
  <code>local   all       all                                   md5</code><br>
  <code>sudo -i -u postgres</code><br>
  <code>[postgres@server ~$] psql</code><br>
  <code>postgres=# ALTER USER postgres PASSWORD 'postgres';</code><br>
  <code>ALTER ROLE</code><br>
  <code>postgres=# /q</code><br>
  <code>exit</code><br>
  <li>In file pg_indent.conf set your system username with command whoami in terminal and change "default-user"</li>
  <code># MAPNAME       SYSTEM-USERNAME         PG-USERNAME</code><br>
  <code>user1             default-user               postgres</code><br>
  <li>Now you can use passwords added by docker</li>
  <li style="color:red;">Remamber after all reset your postgres</li>
  <code>sudo systemctl restart postgresql-15</code><br>
  <li>Run your database local</li>
  <code>docker-compose up db --build</code>
  <li>To navigate your server local you can use this commands</li>
  <code>docker-compose start db #run database</code><br>
  <code>docker-compose stop db #stop database</code>
  <li>Now you can connect your database</li>
  <li>Run SQL Shell (installed with PostgreSQL) or installed pgAdmin (can install with PostgreSQL) or preferred DBeaver</li>
  <li>To your connection in Dbeaver or other you use:</li>
  <code>Host: localhost</code><br>
  <code>Port: 5433</code><br>
  <code>Database: job-schedule</code><br>
  <code>Username: job-schedule</code><br>
  <code>Password: django-app</code><br>
  <li>all configs you can add and change in file ./envs/postgres.env, but remember to again --build app</li>
</ol>

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
```

or for dev

```bash
pipenv install [package] --dev
```

### install develop packages

```bash
  cd backend
  pipenv install --dev
```

run local develop script

```bash
  cd backend
  ./dev_valid.sh
```

run local develop script in docker container if change build directory

```bash
  docker-compose -f docker-compose.tests.yml up --build
```

or use only docker-compose up

```bash
  docker-compose -f docker-compose.tests.yml up
```

coverage html

```bash
  start ./htmlcov/index.html
```
