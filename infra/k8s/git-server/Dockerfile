FROM python:3.7-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install git-core nginx fcgiwrap -y
RUN update-rc.d fcgiwrap enable

COPY git-server.conf /etc/nginx/sites-enabled/default

USER root
RUN chown -Rf www-data:www-data "/srv"

CMD service fcgiwrap start && nginx -g "daemon off;"