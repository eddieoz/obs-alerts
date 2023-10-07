# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install Flask Flask-SocketIO eventlet

# Make port 5002 available to the world outside this container
EXPOSE 5002

# Define environment variable to tell Flask to run on a specific port
ENV FLASK_RUN_PORT=5002
ENV API_KEY = "<INSERT YOUR API KEY HERE>"

# Run the application
CMD ["python", "app.py"]