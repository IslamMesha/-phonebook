FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

EXPOSE 8000

RUN pip install -r requirements.txt
