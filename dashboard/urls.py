from dashboard.views import doctor_dashboard
from django.urls import path

urlpatterns = [  
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),  
]