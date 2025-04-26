from django.urls import path
from .views import RegistrationView
from .views import MeView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('me/', MeView.as_view(), name='me'),
]
