FROM python:3.10

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install poetry
COPY main.py Makefile pyproject.toml poetry.lock .env /app/
RUN apt-get update && apt-get install -y build-essential portaudio19-dev
RUN poetry install --no-root
COPY src/ /app/src/
EXPOSE 8000

CMD ["make", "run"]
