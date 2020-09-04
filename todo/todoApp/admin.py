from django.contrib import admin

# Register your models here.
from .models import Todo
from tinymce.widgets import TinyMCE
from django.db import models

class TodoAdmin(admin.ModelAdmin):
    """
    fields = [
        "text",
        "added_date",
        "Discreption"
    ]
    """
    fieldsets = [
        ("What to do?", {"fields": ["text"]}),
        ("Complete Before",{"fields":["added_date"]}),
        #("Series", {'fields': ["Series"]}),
        ("Discreption",{"fields":["discreption"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

#admin.site.register(Series)
#admin.site.register(Category)
admin.site.register(Todo,TodoAdmin)