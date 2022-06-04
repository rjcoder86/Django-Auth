from django.urls import path
from .views import RegistrationView, LoginView, index

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('',index, name='index'),
]