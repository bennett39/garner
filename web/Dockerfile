FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y vim

RUN mkdir -p /src /var/log/django
WORKDIR /src

# Add our dependencies
ADD requirements.txt /src/
RUN pip install -r requirements.txt

ADD . /src/
