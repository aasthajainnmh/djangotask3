from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name= 'index'),
    # path('appointment/',include('appointment.urls')),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('create_post/', views.create_post, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('post_list/', views.post_list, name='customer'),
    path('post_list/<str:category>/',views.patient_dashboard,name='customer'),
    # path('doctor_form/',views.add_doctor,name='doctor_details'),
    path('doctor_details/',views.doctor_details,name='doctor_details1'),
    path('appointment_request/',views.appointment_request,name='appointment_request'),
    path('appointment_details/',views.appointment_details,name='appointment_details'),
    path('create_event/', views.create_calendar_event, name='create_event'),
    path('view_events/', views.view_calendar_events, name='view_calendar_events'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)