# Generated by Django 4.1 on 2022-08-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=50)),
                ('visitor_email', models.EmailField(max_length=254)),
                ('visitor_phone', models.CharField(max_length=12)),
                ('property_enquired', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
            options={
                'verbose_name': 'Enquiry',
                'verbose_name_plural': 'Enquiries',
            },
        ),
    ]