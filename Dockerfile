# `python-base` sets up all our shared environment variables
FROM python:3.12-slim as python-base

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy dependency files first (better caching)
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
COPY README.md ./
COPY . .

RUN poetry install --without dev

RUN poetry install

# WORKDIR /app
# COPY . /app

EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]