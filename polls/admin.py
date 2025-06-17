from django.contrib import admin
from .models import Question,Choice

# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice)


# class QuestionAdmin(admin.ModelAdmin):
#     fields=["pub_date","question_text"]

# You’ll follow this pattern – create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.

# class ChoiceInline(admin.StackedInline):
#     model=Choice
#     extra=2

# One small problem, though. It takes a lot of screen space to display all the fields for entering related Choice objects. For that reason, Django offers a tabular way of displaying inline related objects. To use it, change the ChoiceInline declaration to read:


class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2


class QuestionAdmin(admin.ModelAdmin):
    # The first element of each tuple in fieldsets is the title of the fieldset.
    fieldsets=[
        (None,{"fields":["question_text"]}),
        ("Date information", {"fields":["pub_date"],"classes":["collapse"]}),
              ]
    inlines=[ChoiceInline]
    list_display=["question_text","pub_date","was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
admin.site.register(Question,QuestionAdmin)

# This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”

# It works like this: There are three slots for related Choices – as specified by extra – and each time you come back to the “Change” page for an already-created object, you get another three extra slots.



# Now that the Question admin page is looking good, let’s make some tweaks to the “change list” page – the one that displays all the questions in the system.

# By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display individual fields. To do that, use the list_display admin option, which is a list of field names to display, as columns, on the change list page for the object:
# \
# You can click on the column headers to sort by those values – except in the case of the was_published_recently header, because sorting by the output of an arbitrary method is not supported. Also note that the column header for was_published_recently is, by default, the name of the method (with underscores replaced with spaces), and that each line contains the string representation of the output.

# You can improve that by using the display() decorator on that method (extending the polls/models.py file that was created in Tutorial 2),