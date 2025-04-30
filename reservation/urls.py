from django.urls import path
from .views import *

urlpatterns = [
    path('appointments/book/', CreateReservation.as_view(), name='create_appointment'),
    path('appointments/', GetReservation.as_view(), name='list_appointment'),  
    path('appointments/<int:pk>/',HandleAppointment.as_view(), name='edit_appointment'), 
    path('booked_slots/<int:doctor_id>/<str:date>/',booked_slots,name='notbooked_slots'),
]
