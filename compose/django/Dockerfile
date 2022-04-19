FROM python:3.9-slim-bullseye
ENV APP_HOME='/app'
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VERSION='1.1.12'
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # Translations dependencies
  gettext \
  # psycopg2 dependencies
  libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
COPY ./poetry.lock .
COPY ./pyproject.toml .
# packages manager
RUN pip install poetry
RUN poetry install
WORKDIR ${APP_HOME}
RUN addgroup --system django \
    && adduser --system --ingroup django django
COPY --chown=django:django ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
COPY --chown=django:django ./compose/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
COPY --chown=django:django ./application ${APP_HOME}/
# make django owner of the WORKDIR directory as well.
RUN chown django:django ${APP_HOME}
USER django

ENTRYPOINT ["/entrypoint"]
