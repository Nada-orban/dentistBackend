# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import AbstractUser

# class Signup (AbstractUser):
#     username = models.CharField(max_length=150, unique=True, default="default_user")
#     first_name=models.CharField(max_length=20,default="")
#     last_name=models.CharField(max_length=20,default="")
#     age= models.IntegerField(
#         validators=[MinValueValidator(1), MaxValueValidator(120)],  # Restrict age between 1-120
#           # Allows the field to be optional
#     ),
#     address= models.TextField(max_length=200,null=True, blank=True)
#     email= models.EmailField(max_length=100,null=True, blank=True)
#     password=models.CharField(max_length=128,default="")
    
    
  
#     def save(self, *args, **kwargs):
#       """ Hash the password before saving the user """
#       self.password = make_password(self.password)  # ✅ Hashes the password securely
#       super().save(*args, **kwargs)
#     def __str__(self):
#         return self.username

# Create your models here.
