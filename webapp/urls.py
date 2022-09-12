from django.urls import path
from webapp.views import *

app_name = 'webapp'
urlpatterns = [
    path('', index, name='index'),
    path('cars', VehicleListView.as_view(), name='cars'),
    path('about_us', about_us, name='about_us'),
    path('contact_us', contact_us, name='contact_us'),
    path('register', register_user, name='register'),
    path('logs', LogEntryAdmin.as_view(), name='logs'),
]
