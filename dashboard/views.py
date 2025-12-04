from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from doctors.models import Doctors
from rest_framework.views import APIView
from reservation.models import Booking 
from dashboard.models import Patient,PatientHistory
from .serializers import DoctorDashboardSerializer,BookingDashboardSerializer,PatientDashboardSerializer,PatientHistoryDashboardSerializer



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
  
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_dashboard(request):
  user=request.user
  
  # If user is a patient
  if hasattr(user, 'patient_profile'):
      patient = user.patient_profile
      patient_data = PatientDashboardSerializer(patient).data
      history_entries = PatientHistory.objects.filter(patient=patient)
      history_data = PatientHistoryDashboardSerializer(history_entries, many=True).data
      return Response({
            "patient": patient_data,
            "history_entries": history_data
      })
      

    # If user is staff: return all patients and histories
  elif user.is_staff:
      patients = Patient.objects.all()
      patient_data = PatientDashboardSerializer(patients, many=True).data
      history_entries = PatientHistory.objects.all()
      history_data = PatientHistoryDashboardSerializer(history_entries, many=True).data
      # return Response({
      #       "patients": patient_data,
      #       "history_entries": history_data
      # })
      return Response(patient_data)

  else:
      return Response({"error": "You are not authorized to view this data."}, status=403)
  
  # if hasattr(user,'patient_profile'):
  #   patient= user.patient_profile
  # elif user.is_staff:
  #   patient_id = request.query_params.get('patient_id')
  #   if not patient_id:
  #     return Response({"error": "Missing patient_id for staff access."}, status=400)
  #   try:
  #     patient = Patient.objects.get(id=patient_id)
  #   except Patient.DoesNotExist:
  #     return Response({"error": "Patient not found."}, status=404)
  # else:
  #     return Response({"error": "You are not a patient and not authorized staff."}, status=403)
  
  # patientData= PatientDashboardSerializer(patient).data
  # PatientHistory=PatientHistory.objects.filter(patient=patient)
  # historySAerilaizer=PatientHistoryDashboardSerializer(PatientHistory,many=True).data
  # return Response({
  #       "patient": patientData,
  #       "history_entries": historySAerilaizer
  # })

  
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_patient(request):
  user=request.user
  if user.patient_profile.exists():
    return Response({"error": "Patient profile already exists."}, status=400)
  data=request.data
  serializer=PatientDashboardSerializer(data=data)
  if serializer.is_valid():
    serializer.save(user=user)
    return Response(serializer.data,status=201)
  return Response(serializer.errors,status=400)


class updatepatient(APIView):
  permission_classes=[IsAuthenticated]
  
  def get_patient(self,pk):
    try:
      return Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
      return None

    
  def update_patient(self,request,pk):
    patient=self.get_patient(pk)
    if not patient:
      return Response({"error":"Patient not found."},status=404)
    data=request.data
    serializer=PatientDashboardSerializer(patient,data=data,partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=400)
  
  def get_patient_history(self,pk):
    patient=self.get_patient(pk)
    try:
      return PatientHistory.objects.filter(patient=patient)
    except PatientHistory.DoesNotExist:
      return None
    
  def update_history(self,request,pk):
    history_entries=self.get_patient_history(pk)
    if history_entries is None or not history_entries.exists():
      return Response({"error":"No history entries found for this patient."},status=404)
    data=request.data
    serializer=PatientHistoryDashboardSerializer(history_entries,data=data,partial=True,many=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=400)