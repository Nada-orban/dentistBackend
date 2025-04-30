from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view,permission_classes


class CreateReservation(APIView):
  def post(self,request):
      doctorId=request.data.get('doctor')
      date = request.data.get('appointment_date')
      time = request.data.get('appointment_time')
      
      exists = Booking.objects.filter(
      doctor_id=doctorId,
      appointment_date=date,
      appointment_time=time
      ).exists()
      
      if exists:
        raise ValidationError("This appointment slot is already taken.")
      
      
      serializer=BookingSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
  
class GetReservation(APIView):
  def get(self,request):
    user = request.user
   
    if user.is_staff:
      reservations=Booking.objects.all()
    else:
      reservations=Booking.objects.filter(doctor= user.doctor_profile)
      
      
      
    serializer=BookingSerializer(reservations,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
        
    
@api_view(['GET'])
def booked_slots(request, doctor_id, date):
    bookings = Booking.objects.filter(doctor_id=doctor_id, appointment_date=date)
    booked_times = bookings.values_list('appointment_time', flat=True)
    return Response(booked_times)

class HandleAppointment(APIView):
  def get_object(self,pk):
    try:
      reservation=Booking.objects.get(pk = pk)
      return reservation
    except Booking.DoesNotExists:
      return None
    
  def get(self,request,pk):
    reservation = self.get_object(pk)
    if reservation is None:
      return Response({"error": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookingSerializer(reservation)
    return Response(serializer.data)
  
  def patch(self,request,pk):
    reservation = self.get_object(pk)
    if reservation is None:
      return Response({"error": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookingSerializer(reservation,data=request.data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,pk):
    reservation = self.get_object(pk)
    if reservation is None:
      return Response({"error": "Reservation not found"}, status=status.HTTP_404_NOT_FOUND)
    reservation.delete()
    return Response({"message": "Reservation deleted successfully"},status=status.HTTP_204_NO_CONTENT)

   
    
   
    
   
    


# Create your views here.
