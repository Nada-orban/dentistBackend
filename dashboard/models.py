from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
  user=models.OneToOneField(User,related_name='patient_profile',on_delete=models.CASCADE,null=True,blank=True)
  patient_name=models.CharField(max_length=255)
  age=models.IntegerField()
  email = models.EmailField(unique=True)
  phone=models.CharField(max_length=15, unique=True)
  gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
  address = models.CharField(max_length=255, null=True, blank=True)
  doctor=models.ForeignKey('doctors.Doctors',on_delete=models.CASCADE,related_name='patients', null=True,blank=True)
  # medical_history = models.TextField(null=True, blank=True)
  allergies = models.TextField(null=True, blank=True)
  medications = models.TextField(null=True, blank=True)
  emergency_contact = models.CharField(max_length=15, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_patients')
  last_updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
        return self.patient_name
      
      
class PatientHistory(models.Model):
  patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='history_entries')
  notes = models.TextField()
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"History for {self.patient.patient_name} on {self.created_at.date()}"
      
      