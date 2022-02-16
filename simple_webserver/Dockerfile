FROM python:3.8.12-slim-buster
COPY app.py /
COPY requirements.txt /
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]