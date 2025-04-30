from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The reviewer
    reviewed_item = models.CharField(max_length=255)  # Can be linked to another model if needed
    rating = models.PositiveIntegerField(default=1)  # Rating (1-5)

# Create your models here.
