# Generated by Django 4.0.3 on 2022-07-13 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_author_book_page_number'),
        ('student', '0006_book_student_is_returned_student_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book_Student',
            new_name='BookStudent',
        ),
    ]
