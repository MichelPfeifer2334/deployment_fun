FROM python:3.12-slim-trixie

WORKDIR /app
RUN pip install --no-cache-dir poetry
ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock ./
RUN poetry install --only main --no-interaction

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]