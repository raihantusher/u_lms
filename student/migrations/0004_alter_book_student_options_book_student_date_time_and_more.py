# Generated by Django 4.0.3 on 2022-06-19 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book_student',
            options={'verbose_name': 'Book n Student'},
        ),
        migrations.AddField(
            model_name='book_student',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_student',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]