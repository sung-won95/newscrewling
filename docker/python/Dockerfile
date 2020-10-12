FROM python:3.8

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
ENV PYTHONUNBUFFERED=0

RUN apt-get update && apt-get install -y g++ default-jdk

COPY python/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /module
