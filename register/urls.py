from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register_user,logout_user, CustomAuthToken

urlpatterns = [
    path('signup/', register_user, name='signup'),
    path('signin/', register_user, name='signin'),  
    
    path('logout/', logout_user, name='logout_user'),
]
