
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev --no-root

CMD ["gunicorn", "wsgi:new_app", "-b", "0.0.0.0:5000"]