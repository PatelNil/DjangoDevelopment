# Generated by Django 3.1.1 on 2020-09-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_todo_discreption'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='active_user',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
