from django.shortcuts import render
from .models import Doctors
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DoctorsSerializers
from rest_framework.decorators import api_view ,parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET'])
def get_Doctors(request):
    DoctorsList = Doctors.objects.all()  # Get all records
    serializer = DoctorsSerializers(DoctorsList, many=True)  # Serialize data
    return Response(serializer.data)  # Return JSON response

# Create your views here.
@api_view(['post'])
@parser_classes([MultiPartParser, FormParser])
def post_Doctors(request):
    serializer=DoctorsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HandleDoctor(APIView):
    def get_object(self,pk):
        try:
            doctor=Doctors.objects.get(pk = pk)
            return doctor
        except Doctors.DoesNotExists:
            return None
    
    def get(self,request,pk):
        doctor = self.get_object(pk)
        if doctor is None:
            return Response({"error": "doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorsSerializers(doctor)
        return Response(serializer.data)

    def patch(self,request,pk):
        doctor = self.get_object(pk)
        if doctor is None:
            return Response({"error": "doctor not found"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = DoctorsSerializers(doctor,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
    def delete(self,request,pk):
        doctor = self.get_object(pk)
        if doctor is None:
            return Response({"error": "doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        doctor.delete()
        return Response({"message": "doctor deleted successfully"},status=status.HTTP_204_NO_CONTENT)