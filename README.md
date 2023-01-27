# Job-schedule

## To run local and deploy needed

[Python](https://www.python.org/downloads/)\
[Docker](https://docs.docker.com/compose/install/)

## Run Locally

Clone the project

```bash
  git clone https://github.com/kwiats/job-schedule job-schedule
```

Go to the project directory

```bash
  cd job-schedule/backend
```

Install pipenv

```bash
  pip install pipenv
```

Install dependencies

```bash
  pipenv install --system
```

Go to the shell

```bash
  pipenv shell
```

Start the server

```bash
  python3 manage.py runserver_plus
```

## Deployment

To deploy this project run

```bash
  git clone https://github.com/kwiats/job-schedule job-schedule
```

Go to the project directory

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

## Install packages

```bash
cd backend
pipenv install [package]
```

or for dev

```bash
pipenv install [package] --dev
```
