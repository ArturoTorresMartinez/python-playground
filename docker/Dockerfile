# Define an alias for the specific python version used in this file.
FROM python:3.11.3-slim as python

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app/python_playground

# Install Django
RUN pip install django

# Copy the rest of the source code from your host to your image filesystem.
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application:
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
