# Pull base image
FROM python:3.7-slim


# Ser environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set work directory
WORKDIR /code


# Install Dependencies 
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system


# Copy project 
COPY . /code
