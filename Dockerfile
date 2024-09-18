FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.pip .
RUN pip install -r requirements.pip

COPY . . 