# Generated by Django 4.0.3 on 2022-07-14 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_bookstudent_fine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookstudent',
            name='fine',
        ),
    ]
