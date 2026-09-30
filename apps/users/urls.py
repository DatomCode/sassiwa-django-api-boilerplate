from django.urls import path
from apps.users.views import UserRegistration
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
]