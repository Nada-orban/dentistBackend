from django.contrib.auth.models import User
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
import traceback
import logging
# from .models import Signup
# from .serializers import SignupSerializer

logger = logging.getLogger(__name__)


#signin and signup
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username=request.data.get('username')
    password=request.data.get('password')
    
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid credentials."}, status=400)
    token, _ = Token.objects.get_or_create(user=user)
    is_doctor = hasattr(user, 'doctor_profile')
    is_admin = user.is_staff or user.is_superuser
    return Response({
        'message': 'Login successful',
        'user_id': user.id,
        'username': user.username,
        'token': token.key,
        'role': 'doctor' if is_doctor else 'admin' if is_admin else 'user',
    })
    
    # serializerdata=RegisterSerializer(data=request.data)
    
    # if serializerdata.is_valid():
    #     try:
    #         user = serializerdata.save()                       # ← creates & saves user
    #         token, _ = Token.objects.get_or_create(user=user)
            
    #         is_doctor = hasattr(user, 'doctor_profile')
    #         is_admin = user.is_staff or user.is_superuser  # or your custom admin field
    #         return Response(
    #             # {
    #             #     "message": "User created successfully",
    #             #     "user_id": user.id,
    #             #     "token": token.key,
    #             #     'role': 'doctor' if is_doctor else 'admin' if is_admin else 'user',
    #             # }
    #             {
    #         'message': 'Login successful',
    #         'user_id': user.id,
    #         'username': user.username,
    #         'token': token.key,
    #         'role': 'doctor' if is_doctor else 'admin' if is_admin else 'user',
    #     }
    #             # ,
    #             # status=status.HTTP_201_CREATED,
    #             )
    #     except Exception as e:
    #         traceback.print_exc() 
    #         logger.exception("Error during user registration")# ← will show full error in logs
    #         return Response({"error": str(e)}, status=500)

    # else:
    #     # ✅ move .errors here
    #     logger.warning(f"Validation errors: {serializerdata.errors}")
    #     return Response(serializerdata.errors, status=400)  
    
   #logout
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.exception("Error during logout")
        return Response({"error": str(e)}, status=500)
    