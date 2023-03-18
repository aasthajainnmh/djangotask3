from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from datetime import time

specialization = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy')
)

class User(AbstractUser):
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    },default='patient')
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='images/')
    specialization = models.CharField(max_length=255)
    
class Post(models.Model):
    CATEGORY_CHOICES=(
        ('Mental Health','Mental Health'),
        ('Heart Diseases','Heart Diseases'),
        ('Covid19','Covid19'),
        ('Immunization','Immunization'),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    summary=models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=True)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    appointment_date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default='00:00:00')
    end_time = models.TimeField(default=time(minute=45))
    
class TakeAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    specialization=models.CharField(max_length=100,default='')
    start_time = models.TimeField(default='00:00:00')
    date_of_appointment = models.DateField(default=timezone.now)

class PatientsRequiredDetails(models.Model):
    doctor_name=models.CharField(max_length=100,default='')
    specialization=models.CharField(max_length=100,default='')
    date_of_appointment = models.DateField(default=timezone.now)
    start_time = models.TimeField(default='00:00:00')
    