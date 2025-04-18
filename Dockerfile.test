# Use the official Python 3 image as the base image
FROM python:3

LABEL maintainer="Brian-Schmiedt@fglife.com"

# Set up the working directory
WORKDIR /DockerPytest

# Copy dependencies first for efficient caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ARG and ENV for dynamic variables
ARG TAGNAME="Regression"
ENV TAGNAME=${TAGNAME} 

# Force the build to process the ARG dynamically
RUN echo "Building with TAGNAME=${TAGNAME}"

# Copy the rest of the application files
COPY . .