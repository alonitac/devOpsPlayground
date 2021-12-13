FROM python:3.8.12-slim-buster
#ARG DEBIAN_FRONTEND=noninteractive
RUN echo "build started..."
RUN apt update
RUN apt install git -y
RUN pip install "python-telegram-bot>=13.8.1" "youtube-dl>=2021.6.6"

WORKDIR /app
COPY youtubeBot/ .

RUN git clone https://github.com/alonitac/devOpsPlayground.git

CMD ["python3", "bot.py"]

