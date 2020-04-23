# Pull Base Image
FROM python:3.7-slim

#Set ENVIRONMENT VARIABLES

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# SET WORK DIRECTORY
WORKDIR /code

# INSTALL DEPENDENCIES
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#copy project

COPY . /code/