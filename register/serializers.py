# from rest_framework import serializers
# from .models import Signup
# from django.contrib.auth.hashers import make_password

# class SignupSerializer(serializers.ModelSerializer):
#     confirmed_password = serializers.CharField(write_only=True)  # ✅ Only exists in the request, not in DB

#     class Meta:
#         model = Signup
#         fields = ["first_name", "last_name", "age", "address", "email", "password", "confirmed_password"]
#         extra_kwargs = {
#             "password": {"write_only": True}  # ✅ Hide password in responses
#         }

#     def validate(self, data):
#         """ Check if password and confirmed_password match before saving """
#         if data["password"] != data["confirmed_password"]:
#             raise serializers.ValidationError({"password": "Passwords do not match!"})
        
#         data["password"] = make_password(data["password"])  # ✅ Hash password before saving
#         del data["confirmed_password"]  # ✅ Remove confirmed_password before saving
        
#         return data