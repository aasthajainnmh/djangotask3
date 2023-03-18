from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Post
from .models import Doctor
from .models import PatientsRequiredDetails

CATEGORY_CHOICES=(
        ('Mental Health','Mental Health'),
        ('Heart Diseases','Heart Diseases'),
        ('Covid19','Covid19'),
        ('Immunization','Immunization'),
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    profile_photo = forms.ImageField(required=False)
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('profile_photo','firstname','lastname', 'username', 'email', 'password1', 'password2', 'is_admin', 'address', 'is_customer')
        
class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    image = forms.ImageField(required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = Post
        fields =('title', 'image','category','summary','content','is_draft')
class Doctor_Details(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    profile_picture = forms.ImageField(required=False)
    specialization = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = Doctor
        fields = ('name','profile_picture','specialization')


class PatientsRequiredDetails(forms.ModelForm):
    doctor_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    specialization = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    date_of_appointment = forms.DateTimeField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "datetime-local"
            }
        )
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "type": "time"
            }
        )
    )

    class Meta:
        model = PatientsRequiredDetails
        fields = [
            "doctor_name",
            "specialization",
            "date_of_appointment",
            "start_time"
        ]
    