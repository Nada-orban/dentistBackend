from django.db import models

class ContactForm(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField(blank=True,null=True)
	message = models.TextField()

  

	def __str__(self):
		return self.full_name     

# Create your models here.
