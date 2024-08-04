from django.urls import path
from .views import register_user, user_login, user_logout, csrf_token  # Not csrf-token

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('csrf-token/', csrf_token, name='csrf_token'),  # Correct view name
]
