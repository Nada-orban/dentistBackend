from django.contrib.auth.models import User
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny ,IsAuthenticated
# from .models import Signup
# from .serializers import SignupSerializer




#signin and signup
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    first_name  = request.data.get("first_name")
    last_name   = request.data.get("last_name")
    # age=request.data.get("age")
    # address=request.data.get("address")
    
    

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
        last_name=last_name)

    # ✅ Generate and return a token for the user
    token, created = Token.objects.get_or_create (user=user)

    return Response({
        "message": "User created successfully",
        "user_id": user.id,
        "token": token.key
    }, status=status.HTTP_201_CREATED)
    
# logout
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])  # ✅ Only authenticated users can log out
# def logout_user(request):
#     request.user.auth_token.delete()  # ✅ Delete the token
#     return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)