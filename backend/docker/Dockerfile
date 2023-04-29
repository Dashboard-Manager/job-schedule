ARG PYTHON_VERSION=3.10.7
ARG PYTHON_TYPE=slim-bullseye

###########
# PREPARE #
###########


FROM python:${PYTHON_VERSION}-${PYTHON_TYPE} as python

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential

# Set environment variables
ENV POETRY_VERSION=1.3.2

# Install poetry
RUN pip install poetry==$POETRY_VERSION --no-cache-dir

# Add linter configs
COPY setup.cfg .isort.cfg ./

# RUN mkdir celery && chmod +x /celery
COPY ./docker/dev/celery/* ./celery/
RUN sed -i 's/\r$//g' celery/*.sh
RUN chmod +x ./celery/*.sh

COPY ./docker/dev/django.sh /django-commands.sh
RUN sed -i 's/\r$//g' /django-commands.sh && chmod +x /django-commands.sh

# Set the entrypoint script
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh

###########
# BUILDER #
###########

# Python build stage
FROM python as python-build-stage

ARG APP_HOME=/src
WORKDIR ${APP_HOME}

# Copy the poetry.lock and pyproject.toml files.
COPY ./poetry.lock ./pyproject.toml ./

# Install poetry
COPY ./requirements.txt .
RUN poetry export --with production --with dev -f requirements.txt --output requirements.txt
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
    -r requirements.txt

###########
# EXECUTE #
###########

# Python 'run' stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=dev
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_HOME=/src
WORKDIR ${APP_HOME}

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    # translations dependencies
    gettext \
    # Additional dependencies
    procps \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy the installed packages from the python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# Copy the rest of the application code to the container
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint.sh"]
