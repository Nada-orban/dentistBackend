from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    appointment_date = serializers.DateField(
        format="%Y-%m-%d",  # ✅ Enforces correct format
        input_formats=["%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"],  # ✅ Accepts multiple formats
        required=False, allow_null=True  # ✅ Allows optional date
    )

    class Meta:
        model = Booking
        fields =  "__all__"
        
        
   
      

  