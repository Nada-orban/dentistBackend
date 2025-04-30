from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register_user

urlpatterns = [
    path('signup/', register_user, name='signup'),
    path('signin/', obtain_auth_token, name='signin'),  
    # path('api/logout/', logout_user, name='logout_user'),
]
