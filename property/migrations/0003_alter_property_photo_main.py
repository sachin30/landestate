# Generated by Django 4.1 on 2022-09-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_property_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='photo_main',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]