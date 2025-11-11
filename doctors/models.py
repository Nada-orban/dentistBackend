from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

DAYS_OF_WEEK = [
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
]

class Doctors (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile', null=True,blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    specialization = models.CharField(max_length=100)  # E.g., Dentist, Cardiologist
    experience_years = models.PositiveIntegerField(null=True, blank=True, default=0)  # Years of experience
    available_days =MultiSelectField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField(null=True, blank=True)  # When the doctor starts seeing patients
    end_time = models.TimeField(null=True, blank=True)  # When the doctor stops seeing patients
    bio = models.TextField(null=True, blank=True)  # Short description
    profile_image = models.ImageField(upload_to='doctor_profiles/', null=True, blank=True)
    is_active = models.BooleanField(default=True)  # If the doctor is available for bookings

    def __str__(self):
        return f"Dr. {self.full_name} - {self.specialization}"
    
    def save(self, *args, **kwargs):
        if self.full_name:
            # self.full_name = self.full_name.capitalize()
            self.full_name = self.full_name.title()      
        super().save(*args, **kwargs)


