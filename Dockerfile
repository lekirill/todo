FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD . /app/