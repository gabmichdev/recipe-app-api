FROM python:3.7
LABEL Gabriel Michel

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apt-get update
RUN apt-get install postgresql postgresql-contrib -y
RUN apt-get install gcc libc-dev -y

RUN pip install -r /requirements.txt

RUN mkdir  /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user