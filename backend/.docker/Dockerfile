FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /src

COPY Pipfile Pipfile.lock /src/
RUN pip install pipenv && pipenv install --system

RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev 

COPY . /src/
