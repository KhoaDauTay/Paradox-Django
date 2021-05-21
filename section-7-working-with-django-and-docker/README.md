# Section 7: Working with Django and Docker
## How to Set Up Django with Docker
- Step 1: Setting virtual enviroment
    ```
    python3.8 -m venv venv
    ```
    - Notes: Use your python version. mine is python 3.8.10

- Step 2: Activate the virtualenv you have just created:

    ```
    source <virtual env path>/bin/activate
    ```
- Step 3: Using Pip install django and django rest

    ```
    pip3 install django
    pip3 install djangorestframework
    ```
- Step 4: Create app name is `tutorial`

    ```
    django-admin startproject tutorial
    ```
- Step 5: Create `Dockerfile`
    - Copy it into file
    ```
    FROM python:3.8.6
    ENV PYTHONUNBUFFERED=1
    WORKDIR /app
    COPY requirements.txt /app/requirements.txt
    RUN pip install -r requirements.txt
    COPY . /app

    CMD python manage.py runserver 0.0.0.0:8000
    ```
- Step 6: Setup docker compose

    ```
    version: '3.8'
    services:
        web:
            build: 
                context: .
                dockerfile: Dockerfile
            ports: 
                - 8000:8000
            volumes: 
                - .:/app
            depends_on:
                - db
        db:
            image: mysql:5.7.22
            restart: always
            environment:
                MYSQL_DATABASE: admin
                MYSQL_USER: root
                MYSQL_PASSWORD: root
                MYSQL_ROOT_PASSWORD: root
            volumes:
                - .dbdata:/var/lib/mysql
            ports:
                - 33066:3306
    ```
## Connect Django with MySQL with Docker
- Build and run compose :

    ```
    docker-compose up
    ```
- Stop compose:
    ```
    docker-compose down
    ```
- When `docker-compose up`, you can access terminal and run migrate with Mysql:

    ```
    docker-compose exec web python3 manage.py migrate
    ```