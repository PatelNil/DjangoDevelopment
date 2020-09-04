from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
"""
class Todo_Category(models.Model):

    category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)
 
class Todo_Series(models.Model):
    series = models.CharField(max_length=200)

    category = models.ForeignKey(Todo_Category, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series
"""

class Todo(models.Model):
    text = models.CharField(max_length=200)
    discreption = models.TextField(blank=True)
    added_date = models.DateTimeField()
    active_user = models.CharField(max_length=200,blank=True)
    #series = models.ForeignKey(Todo_Series, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.text
