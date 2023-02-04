ARG PYTHON_VERSION=3.11.1-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIPENV_IGNORE_VIRTUALENVS=1

ARG APP_HOME=/src
WORKDIR ${APP_HOME}

COPY Pipfile Pipfile.lock ${APP_HOME}/

RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    && pip install pipenv \
    && pipenv requirements > requirements.txt \
    && pipenv requirements --dev > dev-requirements.txt \
    && pip install -r requirements.txt \
    && pip install -r dev-requirements.txt \
    # cleaning up unused files
    && pipenv lock --clear \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


ADD ./docker/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ADD ./docker/django.sh /django.sh
RUN sed -i 's/\r//' /django.sh
RUN chmod a+x /django.sh

ADD ./dev_valid.sh /dev_valid.sh
RUN sed -i 's/\r//' /dev_valid.sh
RUN chmod a+x /dev_valid.sh

ADD . /setup.cfg
ADD . /.isort.cfg

COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint.sh"]
