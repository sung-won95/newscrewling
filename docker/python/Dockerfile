FROM python:3.8

WORKDIR /usr/src/celery

ENV PYTHONUNBUFFERED=0

COPY python/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /module
