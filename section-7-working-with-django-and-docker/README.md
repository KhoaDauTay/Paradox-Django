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
```
## Connect Django with MySQL with Docker
## Django Rest API CRUD