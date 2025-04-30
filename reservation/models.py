from django.db import models
from datetime import date

class Booking(models.Model):
  doctor=models.ForeignKey("doctors.Doctors",on_delete=models.PROTECT,related_name="appointment", null=True,blank=True)
  full_name=models.CharField(max_length=200,default="")
  age=models.IntegerField(null=True, blank=True)
  email=models.EmailField(max_length=100,null=True, blank=True)
  phone=models.CharField(max_length=15, unique=True,default="")
  appointment_date=models.DateField(default=date.today, null=True, blank=True)
  appointment_time=models.TimeField(null=True, blank=True)
  message=models.TextField(max_length=200,null=True,blank=True)
  


  def __str__(self):
        return f"{self.full_name} - {self.appointment_date} at {self.appointment_time}"


# Create your models here.
