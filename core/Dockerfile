FROM python:3.8.12-alpine3.15
MAINTAINER Rakibul

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .

RUN apk update
RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
