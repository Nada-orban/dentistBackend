from rest_framework import serializers
# from .models import Signup
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User                      # ← existing model
        fields = ["username", "email", "password",
                  "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

