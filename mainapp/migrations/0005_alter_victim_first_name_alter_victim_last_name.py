# Generated by Django 4.0.3 on 2022-03-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_victim_first_name_alter_victim_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='first_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='victim',
            name='last_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
