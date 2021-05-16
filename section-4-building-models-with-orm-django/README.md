# Section 4: Building Models with ORM Django
## Lesson overview
- Learn overview and how to using Models in DJango

## Overview and how to using Models in DJango
### Overview
- Models is similar to table in Database.
- The attributes and data types used by the Model are the fields in the table that are mapped by the ORM, we will see this in more detail in this section.
- Example:
  - Create table Person with Models
    ```
    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
    ```
    - Create table Person with SQL
    ```
    CREATE TABLE myapp_person (
        "id" serial NOT NULL PRIMARY KEY,
        "first_name" varchar(30) NOT NULL,
        "last_name" varchar(30) NOT NULL
    );
    ```
- Notes:
  - An `id` field is added automatically, but this behavior can be overridden
### Using Models
- You need register the model with app in `settings.py`

```
INSTALLED_APPS = [
    #...
    'myapp',
    #...
]
```
- When you add new apps to INSTALLED_APPS, be sure to run `manage.py migrate`, optionally making migrations for them first with `manage.py makemigrations`.

## Fields
### Overview
- Fields are properties of the class that inherits models.Model. They help define the data type for storage in the DB. These subscriptions will be mapped to the colum in the Table.
- Example:
```
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```
### Field types
- These field types are instances that inherit from the Field class created by Django which helps us define the data type under the DB, and the processing before sending to the DB, ex: validation, check...
- Example:
  - CharField: A string field, for small- to large-sized strings.
  - BooleanField: A true/false field.
  - EmailField: A CharField that checks that the value is a valid email address using EmailValidator.
  - ImageField: Inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
  - TextField: A large text field. The default form widget for this field is a Textarea.
### Field options
- With that said, field types contain certain conditions for data processing before they are put into the DB. So there will always be separate arguments for each data type to satisfy certain use-cases. See more [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#common-model-field-options)
- Example:
  - `nulll`: If True, Django will store empty values as NULL in the database. Default is False.
  - `blank`: If True, the field is allowed to be blank. Default is False.(Using in Form)
  - `default`: The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created
  - `unique`: If True, this field must be unique throughout the table.

## Relationships
- Clearly, the power of relational databases lies in relating tables to each other. Django offers ways to define the three most common types of database relationships: many-to-one, many-to-many and one-to-one.
### Many-to-one relationships
### Many-to-many relationships
### One-to-one relationships