FROM python:3.13-alpine
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"
RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    postgresql-dev \
    build-base \
    python3-dev \
    linux-headers \
    libpq \
    curl \
    git
RUN curl -sSL https://install.python-poetry.org | python -
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

COPY . .
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
