from django.contrib import admin
from .models import User,Post,Doctor,PatientsRequiredDetails

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Doctor)
admin.site.register(PatientsRequiredDetails)