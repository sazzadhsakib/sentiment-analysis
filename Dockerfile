# Use the official Python base image
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# Set the working directory in the container
WORKDIR /sentiment-analysis

# # Copy the requirements.txt file to the container
COPY requirements.txt ./requirements.txt

# # Install the project dependencies
RUN apt-get update 
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN rm ./requirements.txt


# Copy the entire project directory to the container
COPY wsgi.py ./wsgi.py
COPY src ./src

#Download the preloaded Setfit model
RUN gdown https://drive.google.com/drive/folders/1DGUiY0_xV9ZKa7BKBjaEMi0-KTChdcMe\?usp\=sharing -O ./src/rnd/models --folder 

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /mnt
USER appuser



