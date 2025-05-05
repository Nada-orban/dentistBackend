from django.contrib.auth.models import User
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny ,IsAuthenticated
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
    serializerdata=RegisterSerializer(data=request.data)
    if serializerdata.is_valid():
        try:
            user = serializerdata.save()                       # ← creates & saves user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": "User created successfully",
                    "user_id": user.id,
                    "token": token.key,
                },
                status=status.HTTP_201_CREATED,
                )
        except Exception as e:
            traceback.print_exc()      # ← will show full error in logs
            return Response({"error": str(e)}, status=500)
    # validation failed – return errors
        # user = serializerdata.save()
        # try:
        #     user = User.objects.create_user(
        #         username=username,
        #         email=email,
        #         password=password,
        #         first_name=first_name,
        #         last_name=last_name,
        #     )
        #     token, _ = Token.objects.get_or_create(user=user)
        #     return Response({
        #         "message": "User created successfully",
        #         "user_id": user.id,
        #         "token": token.key,
        #     }, status=status.HTTP_201_CREATED)
        # except Exception as e:
        # # print full traceback to Railway logs
        #     traceback.print_exc()
        #     return Response({"error": str(e)}, status=500)
      
    return Response(serializerdata.errors, status=400)
   