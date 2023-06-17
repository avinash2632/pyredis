# Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x start.sh

ENTRYPOINT ["/app/start.sh"]

