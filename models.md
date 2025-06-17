# model field reference
### field options

1. **null** : If True, Django will store empty values as NULL in the database. Default is False.

2. **blank** : If True, the field is allowed to be blank. Default is False.

3. **choices** : A mapping or iterable in the format described below to use as choices for this field. If choices are given, they’re enforced by model validation and the default form widget will be a select box with these choices instead of the standard text field.

    If a mapping is given, the key element is the actual value to be set on the model, and the second element is the human readable name. For example:

    ```python
    YEAR_IN_SCHOOL_CHOICES = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior",
    "GR": "Graduate",
    }
    ```

    ```
    from django.db import models
    class Student(models.Model):
        FRESHMAN = "FR"
        SOPHOMORE = "SO"
        JUNIOR = "JR"
        SENIOR = "SR"
        GRADUATE = "GR"
        YEAR_IN_SCHOOL_CHOICES = {
            FRESHMAN: "Freshman",
            SOPHOMORE: "Sophomore",
            JUNIOR: "Junior",
            SENIOR: "Senior",
            GRADUATE: "Graduate",
        }
        year_in_school = models.CharField(
            max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
            default=FRESHMAN,
        )
        def is_upperclass(self):
            return self.year_in_school in {self.JUNIOR, self.SENIOR}
    ```

4. **default** : The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created.

    ```
    def contact_default():
    return {"email": "to1@example.com"}

    contact_info = JSONField("ContactInfo", default=contact_default)
    ```

5. **editable** : If False, the field will not be displayed in the admin or any other ModelForm. It will also be skipped during model validation. Default is True.

6. **error_messages** : The error_messages argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.

7. **help_text** : Extra “help” text to be displayed with the form widget. It’s useful for documentation even if your field isn’t used on a form.

    ```
    help_text = "Please use the following format: <em>YYYY-MM-DD</em>."
    ```
8. __primary_key__ : If True, this field is the primary key for the model.

9. __unique__ : If True, this field must be unique throughout the table.

10. __verbose_name__ : A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces.

### field types

1. **AutoField** : An IntegerField that automatically increments according to available IDs. You usually won’t need to use this directly; a primary key field will automatically be added to your model if you don’t specify otherwise.

2. **BooleanField** : A true/false field.
    The default form widget for this field is CheckboxInput, or NullBooleanSelect if null=True.

3. **CompositePrimaryKey** : A virtual field used for defining a composite primary key.
    This field must be defined as the model’s pk attribute. If present, Django will create the underlying model table with a composite primary key.

4. **CharField** : The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation using MaxLengthValidator. It’s required for all database backends included with Django except PostgreSQL and SQLite, which supports unlimited VARCHAR columns.

5. **DateField** : 

    DateField.auto_now :  Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps. Note that the current date is always used; it’s not just a default value that you can override.

6. **DateTimeField**

7. **DecimalField**

8. **DurationField**

9. **EmailField**

10. **FileField**

11. **URLField**

12. **ForeignKey**

    ```
    from django.db import models


    class Manufacturer(models.Model):
        name = models.TextField()


    class Car(models.Model):
        manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    ```

# model meta options

1. **abstract**: If abstract = True, this model will be an abstract base class.

2. **app_label**: If a model is defined outside of an application in INSTALLED_APPS, it must declare which app it belongs to:
    ```
    app_label = "myapp"
    ```
3. **base_manager_name** : The attribute name of the manager, for example, 'objects', to use for the model’s _base_manager.

4. **db_table**: The name of the database table to use for the model:
    ```
    db_table = "music_album"
    ```
    For example, if you have an app bookstore (as created by manage.py startapp bookstore), a model defined as class Book will have a database table named bookstore_book.

    To override the database table name, use the db_table parameter in class Meta.

5. **db_table_comment** : The comment on the database table to use for this model. It is useful for documenting database tables for individuals with direct database access who may not be looking at your Django code. For example:

    ```
    class Answer(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        answer = models.TextField()

        class Meta:
            db_table_comment = "Question answers"
    ```
6. **default_manager_name** : The name of the manager to use for the model’s _default_manager.

7. **get_latest_by** :  

    ```python
    # Latest by ascending order_date.
    get_latest_by = "order_date"

    #Latest by priority descending, order_date ascending.
    get_latest_by = ["-priority", "order_date"]
    ```
8. **ordering** : The default ordering for the object, for use when obtaining lists of objects:

    ```
    ordering = ["-order_date"]
    ```
    This is a tuple or list of strings and/or query expressions. Each string is a field name with an optional “-” prefix, which indicates descending order. Fields without a leading “-” will be ordered ascending. Use the string “?” to order randomly.

9. **verbose_name**: A human-readable name for the object, singular:

    ```python
    verbose_name = "pizza"
    ```

# model class reference

### Attributes

**objects**: Each non-abstract Model class must have a Manager instance added to it. Django ensures that in your model class you have at least a default Manager specified. If you don’t add your own Manager, Django will add an attribute objects containing default Manager instance. If you add your own Manager instance attribute, the default one does not appear. Consider the following example:

```python
from django.db import models

class Person(models.Model):
    # Add manager with another name
    people = models.Manager()
```
