# Generated by Django 4.1.7 on 2023-03-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_patientsrequireddetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='patient', error_messages={'required': 'Role must be provided'}, max_length=12),
        ),
    ]
