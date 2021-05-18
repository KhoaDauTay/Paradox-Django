# The Paradox Django:
- Journal for Learning Course: The Complete Python Masterclass: Learn Python From Scratch 
https://www.udemy.com/course/python-masterclass-course/
## Link Download: Sign up OneDrive and download course is [here](https://uithcm-my.sharepoint.com/:f:/g/personal/18520917_ms_uit_edu_vn/ElXUPiiDBKxNpt1d8ibNbFUBBSe4Luh5meZOVaMee_1E9A?e=c3svpa)
## Reference:
- This is part of a blog I wrote myself [here](https://github.com/KhoaDauTay/learn-python), the purpose of this repo is to build up my own categories of knowledge taken from my blog due to my internship.
## Description
- Make Web-Applications using Python.
- Build database oriented web apps with Python, PostgreSQL
- Understand all Django concepts

## Day 0
* Setup project skeleton
## Day 1
### Today's progress
- Learn Make Web Applications In Python Using Django (Section 1)
    - Install django with env
    - Create project
    - Create app
    - Overview app
    - MVC/MVT model
### Thoughts
- Need good thinking mind
- Statistical probabilities
- Understand requirements
### Links to work
- [Section 1](section-1-make-web-applications-in-python-using-django/README.md)
## Day 2
### Today's progress
- Learn Make Web Applications In Python Using Django Part 2(Section 1)
    - Learn views in django
    - Learn create database
    - Learn raise Error 404
    - Learn namespace url
    - Learn url pattern
- Learn Make Web Applications In Python Using Django Part 3(Section 1)
    - Learn use template
    - Learn design detail view
    - Learn use static file
    - Learn use form in Django
### Thoughts
### Links to work
- [Section 1](section-1-make-web-applications-in-python-using-django/README.md)
## Day 3
### Today's progress
- Learn Make Web Applications In Python Using Django 3.2 (Section 2)
    - Install Django==3.2
    - Create Project
    - Create app
    - MVC/MVT model web app
    - Database in Django
    - Create view list data
    - Adding data
    - Use admin panel
    - Create new urls and view
    - Connect database
    - Use template
    - Design detail view
    - Use static file
    - Use form in Django
### Thoughts
### Links to work
- [Section 2](section-2-make-web-applications-with-python-using-django-3.2/README.md)
## Day 4
### Today's progress
- Learn Building REST API's with Python and Django (Section 3)
    - Learn about API, REST, Django REST framework
    - Learn create API data in Django by serializers
    - Learn create fields end point by API
    - Learn view API data
- Learn Building REST API's with Python and Django (Section 3)
    - Learn create imagefiled in api
    - Learn search functional api
    - Learn filter api
    - Learn api authorization
### Thoughts
### Links to work
- [Section 3](section-3-building-rest-api's-with-python-and-django/README.md)
## Day 5
### Today's progress
- Learn about topic of Models in Django
### Thoughts
### Links to work
- [Section 4](section-4-building-models-with-orm-django/README.md)
## Day 6
### Today's progress
- Dive into Django Query set
### Thoughts
### Links to work
- [Section 5](section-5-dive-into-django-queryset/README.md)

## Cheatsheet
```py
django-admin check                       # Checks the entire django project for potential problems
django-admin changepassword <username>   # Allows changing a user’s password. It prompts you to enter a new password twice for the given user.
django-admin clearsessions               # Can be run as a cron job or directly to clean out expired sessions.
django-admin collectstatic               # Helps to collect all the static files in the one mentioned directory
django-admin createsuperuser             # Creates a superuser account (a user who has all permissions).
django-admin compilemessages             # Compiles .po files to .mo files for use with builtin gettext support
django-admin createcachetable            # Creates the tables needed to use the SQL cache backend.
django-admin dbshell                     # Runs the command-line client for specified database, or the default database if none is provided.
django-admin diffsettings                # Displays differences between the current settings.py and Django's default settings.
django-admin dumpdata                    # Output the contents of the database as a fixture of the given format (using each model's default manager unless --all is specified).
django-admin flush                       # Removes ALL DATA from the database, including data added during migrations. Does not achieve a "fresh install" state.
django-admin inspectdb                   # Introspects the database tables in the given database and outputs a Django model module.
django-admin loaddata                    # Installs the named fixture(s) in the database.
django-admin makemessages                # Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) a message file in the conf/locale (in the django tree) or locale (for projects and applications) directory. You must run this command with one of either the --locale, --exclude, or --all options.
django-admin help                        # display usage information and a list of the commands provided by each application
django-admin makemigrations              # create new migrations to the database based on the changes detected in the models
django-admin migrate                     # synchronize the database state with your current state project models and migrations
django-admin remove_stale_contenttypes   # Deletes stale content types (from deleted models) in your database.y.
django-admin runserver <port>            # start the development webserver at 127.0.0.1 with the port <port> default 8000
django-admin sendtestemail               # Sends a test email to the email addresses specified as arguments.
django-admin shell                       # Runs a Python interactive interpreter. Tries to use IPython or bpython, if one of them is available. Any standard input is executed as code.
django-admin showmigrations              # Shows all available migrations for the current project.
django-admin sqlflush                    # Returns a list of the SQL statements required to return all tables in the database to the state they were in just after they were installed.
django-admin sqlmigrate                  # Prints the SQL statements for the named migration.
django-admin sqlsequencereset            # Prints the SQL statements for resetting sequences for the given app name(s).
django-admin squashmigrations            # Squashes an existing set of migrations (from first until specified) into a single new one.
django-admin startapp <Appname>          # create a new django application with the specified name
django-admin startproject <ProjectName>  # create a new project directory structure
django-admin testserver                  # Runs a development server with data from the given fixture(s).
django-admin version                     # display the current django version


# *****************************************************************************
# Starting a django project in python3
# *****************************************************************************


# 1. $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python3 get-pip.py						
# 2. $ pip install virtualenv
# 3. $ mkdir django-projects
# 4. $ cd django-projects  
# 5. $ virtualenv venv 								
# 6. $ source venv/bin/activate	
# 7. $ pip install django							
# 8. $ django-admin startproject myproject
# 9. $ django-admin startapp myapp
# 10. $ python manage.py runserver
```