# Generated by Django 4.1.7 on 2023-03-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_doctor_email_remove_doctor_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
