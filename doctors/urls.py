from django.urls import path
from .views import get_Doctors, post_Doctors,HandleDoctor


urlpatterns = [
    path('', get_Doctors, name='get_doctors'),
    path('create/', post_Doctors, name='add_doctors'),
    path('<int:pk>/', HandleDoctor.as_view(), name='edit_doctors'),
    
    
]