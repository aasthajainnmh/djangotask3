from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Post,Doctor
from .forms import PostForm,Doctor_Details
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PatientsRequiredDetails
from .decorators import user_is_patient, user_is_doctor
from django.http import HttpResponseForbidden
from .forms import PatientsRequiredDetails
from django.http import HttpResponse
import datetime
import calendar
import icalendar
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')

def create_post(request):
    form = PostForm(request.POST,request.FILES)
    if request.method == 'POST' and 'btncreate_post' in request.POST:
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            messages.success(request, 'Your blog post was successfully created.')
            return redirect('post_list')
        else:
            messages.error(request, 'There was an error creating your blog post.')
    elif request.method == 'POST' and 'btn_doctor_details' in request.POST:
        # name=request.POST['inpname']
        # profilepicture=request.FILES['inpimage']
        # specialization=request.POST['inpspecialization']
        form2 = Doctor_Details(request.POST,request.FILES)
        if form2.is_valid():
            form2.save()
        # return redirect('doctor_details1')

    else:
        form = PostForm()
        form2 = Doctor_Details()
    return render(request, 'admin.html', {'form': form,'form2':form2})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'customer.html', {'posts': posts})


def customer(request):
    return render(request,'customer.html')

def patient_dashboard(request):
    posts = Post.objects.all()
    category = request.GET.get('category')
    if category:
        posts = Post.objects.filter(category=category)
    categories=Post.CATEGORY_CHOICES
    context={'posts':posts,'categories':categories,'selected_category':category}
    return render(request, 'post_by_category.html', context)

# def add_data(request):
#     if request.method == 'POST':
#         post_form = PostForm(request.POST,request.FILES)
#         doctor_form = Doctor_Details(request.POST)
#         if post_form.is_valid() and doctor_form.is_valid():
#             post = post_form.save()
#             doctor = doctor_form.save()
#             post.save()
#             messages.success(request, 'Your blog post was successfully created.')
#             doctor.save()
#             messages.success(request, 'Your details submitted successfully.')
#     else:
#         post_form = PostForm()
#         doctor_form = Doctor_Details()

#     context = {'post_form': post_form, 'doctor_form': doctor_form}
#     return render(request, 'admin.html', context)
def add_doctor(request):
    print(request.POST)
    if request.method == 'POST':
        name=request.POST['inpname']
        profilepicture=request.FILES['inpimage']
        specialization=request.POST['inpspecialization']
        forms = Doctor_Details(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
    else:
        forms = Doctor_Details()

    return render(request, 'doctor_details.html', {'name':name,'profilepicture':profilepicture,'specialization':specialization})

def doctor_details(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_details.html', {'doctors': doctors})

@login_required
def appointment_request(request):
    if request.method == 'POST':
        letter = PatientsRequiredDetails(request.POST)
        if letter.is_valid():
            post = letter.save()
            messages.success(request, 'Your response is submitted')
            return redirect('appointment_request')
        else:
            messages.error(request, 'Error')
    else:
        letter = PatientsRequiredDetails()
    return render(request, 'appointment_request.html', {'letter': letter})

def appointment_details(request):
    # form_data = PatientsRequiredDetails.objects.last()
    return render(request, 'appointment_details.html')

def create_calendar_event(request):
    if request.method == 'POST':
        form = PatientsRequiredDetails(request.POST)
        if form.is_valid():
            event_date = form.cleaned_data['date_of_appointment']
            event_time = form.cleaned_data['start_time']
            event_datetime = datetime.datetime.combine(event_date, event_time)
            event_end = event_datetime + datetime.timedelta(minutes=45)
            event_title = "Doctor appointment"
            event_description = "Appointment with Doctor"
            
            event = icalendar.Event()
            event.add('summary',event_title)
            event.add('description',event_description)
            event.add('date', event_date)
            event.add('dtstart', event_time)
            event.add('dtend', event_end)
            calendar = icalendar.Calendar()
            calendar.add_component(event)
            filename = f'appointment_{event_date.strftime("%Y-%m-%d")}.ics'
            response = HttpResponse(calendar.to_ical(), content_type='text/calendar')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
    else:
        form = PatientsRequiredDetails()
    return render(request, 'calendar_event.html', {'form': form})

@login_required
def view_calendar_events(request):
    # doctor = get_object_or_404(Doctor, pk=request.user.pk)
    # events = PatientsRequiredDetails.objects.filter(doctor=doctor).order_by('start_time')
    return render(request, 'calendar_view_events.html')