# accounts/urls.py

from django.urls import path
from .views import register_user, user_login, user_logout,csrf-token

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/csrf-token/', csrf_token, name='csrf_token'),
]
