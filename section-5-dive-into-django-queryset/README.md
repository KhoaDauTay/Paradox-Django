# Section 5: Dive into Django Query
## Lesson overview
- Learn overview and how to using Query set in Django with special Case

## filter(**kwargs)
- Returns a new QuerySet containing objects that match the given lookup parameters.

```
Entry.objects.filter(headline='Hello')
```
```
SELECT Entry
WHERE headline = 'Hello'
```
- If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.
    - Code:
    ```
    Poll.objects.get(
        Q(question__startswith='Who'),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
    )
    ```
    - SQL:
    ```
    SELECT * from polls WHERE question LIKE 'Who%'
        AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
    ```
## exclude(**kwargs)
- Returns a new QuerySet containing objects that do not match the given lookup parameters.
    - Code:
    ```
    Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')
    ```
    - SQL:
    ```
    SELECT ...
    WHERE NOT (pub_date > '2005-1-3' AND headline = 'Hello')
    ```
## order_by(*fields)
- By default, results returned by a QuerySet are ordered by the ordering tuple given by the ordering option in the model’s Meta. You can override this on a per-QuerySet basis by using the order_by method
    ```
    Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
    ```
  - Using `name` of filed is Ascending order.
  - Using prefix `-` in front of filed is descending order.
  - Using prefix `?`  is random order.

## reverse()
- Use the reverse() method to reverse the order in which a queryset’s elements are returned. Calling reverse() a second time restores the ordering back to the normal direction.
```
my_queryset.reverse()
```
## values(*fields, **expressions)
- Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable.

- Each of those dictionaries represents an object, with the keys corresponding to the attribute names of model objects.
    ```
    # This list contains a Blog object.
    >>> Blog.objects.filter(name__startswith='Beatles')
    <QuerySet [<Blog: Beatles Blog>]>

    # This list contains a dictionary.
    >>> Blog.objects.filter(name__startswith='Beatles').values()
    <QuerySet [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]>
    ```
## values_list(*fields, flat=False, named=False)
- This is similar to values() except that instead of returning dictionaries, it returns tuples when iterated over. Each tuple contains the value from the respective field or expression passed into the values_list() call — so the first item is the first field

    ```
    >>> Entry.objects.values_list('id', 'headline')
    <QuerySet [(1, 'First entry'), ...]>
    >>> from django.db.models.functions import Lower
    >>> Entry.objects.values_list('id', Lower('headline'))
    <QuerySet [(1, 'first entry'), ...]>
    ```
- If you only pass in a single field, you can also pass in the flat parameter. If True, this will mean the returned results are single values, rather than one-tuples. An example should make the difference clearer:
    ```
    >>> Entry.objects.values_list('id').order_by('id')
    <QuerySet[(1,), (2,), (3,), ...]>

    >>> Entry.objects.values_list('id', flat=True).order_by('id')
    <QuerySet [1, 2, 3, ...]>
    ```
## union(*other_qs, all=False)
- Uses SQL’s UNION operator to combine the results of two or more QuerySets.
    ```
    qs1.union(qs2, qs3)
    ```
    - Notes: Default union() remove all dulicates in two queryset
- To allow duplicate values, use the all=True argument.
    ```
    qs1.union(qs2, qs3,all=True)
    ```
## select_related(*fields)
- Returns a QuerySet that will “follow” foreign-key relationships, selecting additional related-object data when it executes its query.
    ```
    # Hits the database.
    e = Entry.objects.select_related('blog').get(id=5)

    # Doesn't hit the database, because e.blog has been prepopulated
    # in the previous query.
    b = e.blog
    ```
## get_or_create(defaults=None, **kwargs)
- A convenience method for looking up an object with the given kwargs (may be empty if your model has defaults for all fields), creating one if necessary.

- Returns a tuple of (object, created), where object is the retrieved or created object and created is a boolean specifying whether a new object was created.

    ```
    obj, created = Person.objects.get_or_create(
        first_name='John',
        last_name='Lennon',
        defaults={'birthday': date(1940, 10, 9)},
    )
    ```
## update_or_create(defaults=None, **kwargs)
- A convenience method for updating an object with the given kwargs, creating a new one if necessary. The defaults is a dictionary of (field, value) pairs used to update the object. The values in defaults can be callables.

- Returns a tuple of (object, created), where object is the created or updated object and created is a boolean specifying whether a new object was create
    ```
    obj, created = Person.objects.update_or_create(
        first_name='John', last_name='Lennon',
        defaults={'first_name': 'Bob'},
    )
    ```
## bulk_create(objs, batch_size=None, ignore_conflicts=False)
- This method inserts the provided list of objects into the database in an efficient manner (generally only 1 query, no matter how many objects there are), and returns created objects as a list, in the same order as provided:

```
>>> objs = Entry.objects.bulk_create([
...     Entry(headline='This is a test'),
...     Entry(headline='This is only a test'),
... ])
```
- Notes:
  - The model’s save() method will not be called, and the pre_save and post_save signals will not be sent
  - It does not work with child models in a multi-table inheritance scenario
  - It does not work with many-to-many relationships.
  - 
## bulk_update(objs, fields, batch_size=None)
- This method efficiently updates the given fields on the provided model instances, generally with one query:

    ```
    >>> objs = [
    ...    Entry.objects.create(headline='Entry 1'),
    ...    Entry.objects.create(headline='Entry 2'),
    ... ]
    >>> objs[0].headline = 'This is entry 1'
    >>> objs[1].headline = 'This is entry 2'
    >>> Entry.objects.bulk_update(objs, ['headline'])

    ```
- Notes:
  - You cannot update the model’s primary key
  - Each model’s save() method isn’t called, and the pre_save and post_save signals aren’t sent
  - Updating fields defined on multi-table inheritance ancestors will incur an extra query per ancestor.
  - When an individual batch contains duplicates, only the first instance in that batch will result in an update.
## count()
- Returns an integer representing the number of objects in the database matching the QuerySet.

    ```
    # Returns the total number of entries in the database.
    Entry.objects.count()

    # Returns the number of entries whose headline contains 'Lennon'
    Entry.objects.filter(headline__contains='Lennon').count()
    ```
## Field lookups
- Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods filter(), exclude() and get().

### exact
- Exact match. If the value provided for comparison is None, it will be interpreted as an SQL NULL
    - Code:
    ```
    Entry.objects.get(id__exact=14)
    Entry.objects.get(id__exact=None)
    ```
    - SQL

    ```
    SELECT ... WHERE name ILIKE 'beatles blog';
    SELECT ... WHERE name IS NULL;
    ```
### contains
- Case-sensitive containment test.
  - Code:

    ```
    Entry.objects.get(headline__contains='Lennon')
    ```
  - SQL:
    ```
    SELECT ... WHERE headline LIKE '%Lennon%';
    ```
### in
- In a given iterable; often a list, tuple, or queryset. It’s not a common use case, but strings (being iterables) are accepted.
  - Code:

    ```
    Entry.objects.filter(id__in=[1, 3, 4])
    Entry.objects.filter(headline__in='abc')
    ```
  - SQL:

    ```
    SELECT ... WHERE id IN (1, 3, 4);
    SELECT ... WHERE headline IN ('a', 'b', 'c');
    ```
- You can also use a queryset to dynamically evaluate the list of values instead of providing a list of literal values:
  - Code:
    ```
    inner_qs = Blog.objects.filter(name__contains='Cheddar')
    entries = Entry.objects.filter(blog__in=inner_qs)
    ```

  - SQL:

    ```
    SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%')
    ```
### gt
- Greater than.
  - Code:

    ```
    Entry.objects.filter(id__gt=4)
    ```
  - SQL:

    ```
    SELECT ... WHERE id > 4;
    ```
### range
- Range test (inclusive).
  - Code:

    ```
    import datetime
    start_date = datetime.date(2005, 1, 1)
    end_date = datetime.date(2005, 3, 31)
    Entry.objects.filter(pub_date__range=(start_date, end_date))
    ```
  - SQL:

    ```
    SELECT ... WHERE pub_date BETWEEN '2005-01-01' and '2005-03-31';
    ```
### isnull
- Takes either True or False, which correspond to SQL queries of IS NULL and IS NOT NULL, respectively.
  - Code:
    ```
    Entry.objects.filter(pub_date__isnull=True)

    ```
  - SQL:

    ```
    SELECT ... WHERE pub_date IS NULL;
    ```


