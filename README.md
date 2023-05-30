# Python Playground: Django in Docker

This project demonstrates how to set up a Django application running inside a Docker container.

## Prerequisites

You will need Docker installed on your machine. If you haven't installed Docker yet, you can download it from [Docker's official website](https://www.docker.com/get-started).

## Project Structure

The project structure is as follows:

```
python-playground
 ┣ .git
 ┣ app
 ┃ ┗ app.py
 ┣ docker
 ┃ ┗ Dockerfile
 ┣ python_playground
 ┃ ┣ __init__.py
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┗ wsgi.py
 ┣ users
 ┃ ┣ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┣ views.py
 ┣ .dockerignore
 ┣ .gitignore
 ┣ Pipfile
 ┣ Pipfile.lock
 ┣ README.md
 ┗ manage.py
```

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/ArturoTorresMartinez/python-playground.git
```

2. Navigate into the cloned repository:

```bash
cd python-playground
```

3. Navigate into the `docker` directory:

```bash
cd docker
```

4. Build the Docker image:

```bash
docker build -t python_playground .
```

5. Navigate back to the root directory:

```bash
cd ..
```

6. Run the Docker container:

```bash
docker run -p 8000:8000 -v $(pwd):/app python_playground
```

The Django application will now be accessible at `http://0.0.0.0:8000`.

## Developing

When you want to make changes to the Django application, you can do so by editing the files in the `python_playground` directory on your host machine. Changes will be reflected inside the Docker container due to the volume mapping set up in the `docker run` command.

If you add new Python packages to your Django project, remember to rebuild the Docker image with `docker build -t python_playground .` so that the new packages are installed in the Docker container. If you only change Python or Django code (e.g., views, models, templates), you can just use `docker run` to start the Docker container with the updated code.