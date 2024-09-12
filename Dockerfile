FROM python:3.11

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]