# Generated by Django 4.0.3 on 2022-07-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_rename_book_student_bookstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstudent',
            name='is_issued',
            field=models.BooleanField(default=False),
        ),
    ]
