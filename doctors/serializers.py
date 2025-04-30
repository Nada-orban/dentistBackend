from rest_framework import serializers
from .models import Doctors ,DAYS_OF_WEEK

class DoctorsSerializers(serializers.ModelSerializer):
  available_days = serializers.MultipleChoiceField(choices=[day for day, _ in DAYS_OF_WEEK])
  profile_image = serializers.ImageField(use_url=True)
  class Meta:
    model=Doctors
    fields = '__all__' 
    
    
  # def get_profile_image(self, obj):
  #   request = self.context.get('request')
  #   if obj.profile_image and request:
  #           # This builds the full URL (e.g. http://localhost:8000/media/doctor_profiles/filename.jpg)
  #     return request.build_absolute_uri(obj.profile_image.url)
  #   return None