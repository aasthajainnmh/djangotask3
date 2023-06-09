# Generated by Django 4.1.7 on 2023-03-17 14:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_doctor_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('appointment_date', models.DateField(default=django.utils.timezone.now)),
                ('start_time', models.TimeField(default='00:00:00')),
                ('end_time', models.TimeField(default=datetime.time(0, 45))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TakeAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(default='', max_length=100)),
                ('start_time', models.TimeField(default='00:00:00')),
                ('date_of_appointment', models.DateField(default=django.utils.timezone.now)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.appointment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
