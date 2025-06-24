from rest_framework import serializers
from doctors.models import Doctors
from reservation.models import Booking



class DoctorDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'
        
class BookingDashboardSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Booking
        fields = '__all__'
        