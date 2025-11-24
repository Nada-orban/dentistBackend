from dashboard.views import doctor_dashboard,patient_dashboard,create_patient,updatepatient
from django.urls import path

urlpatterns = [  
    path('doctor/', doctor_dashboard, name='doctor_dashboard'), 
    path('patientInfo/', patient_dashboard, name='patient_dashboard'),
    path('addPatient/', create_patient, name='patient_create'),    
    path('patient/<int:pk>/', updatepatient.as_view(), name='edit_patient'),
     
]