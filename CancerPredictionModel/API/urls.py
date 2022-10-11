from django.urls import path, include
from API.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register')
]