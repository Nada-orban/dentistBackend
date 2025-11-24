from rest_framework import serializers
from doctors.models import Doctors
from reservation.models import Booking
from dashboard.models import Patient,PatientHistory



class DoctorDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'
        
class BookingDashboardSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Booking
        fields = '__all__'
        
class PatientDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
        

class PatientHistoryDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = '__all__'
        
        
        