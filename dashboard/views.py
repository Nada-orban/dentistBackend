from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from doctors.models import Doctors
from reservation.models import Booking
from .serializers import DoctorDashboardSerializer,BookingDashboardSerializer



# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_dashboard(request):
  user=request.user
  
  if hasattr(user,'doctor_profile'):
    doctor = user.doctor_profile
    doctor_data = DoctorDashboardSerializer(doctor).data
    appointments=Booking.objects.filter(doctor=doctor)
    appointment_serializer = BookingDashboardSerializer(appointments, many=True).data
    return Response({
            "doctor": doctor_data,
            "appointments": appointment_serializer
        })

  else:
        # If the user is not a doctor, return an error
    return Response({"error": "You are not a doctor."}, status=403)