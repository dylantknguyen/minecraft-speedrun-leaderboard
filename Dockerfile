FROM ubuntu:18.04

RUN mkdir /code
WORKDIR /code

RUN \
  apt-get update && \
  apt-get install -y python3 python3-dev python3-pip && \
  apt-get install -y firefox && \
  apt-get install -y wget cron && \
  rm -rf /var/lib/apt/lists/*

RUN \
  wget "https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz" && \
  tar -xvzf geckodriver* && \
  chmod +x geckodriver && \
  mv geckodriver /usr/local/bin/


COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

COPY cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN cron /etc/cron.d/cron
RUN touch /var/log/cron.log
