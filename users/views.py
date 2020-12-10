from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import CustomUser # Passenger
from .serializers import UserSerializer ,UpdateUserSerializer, ChangePasswordSerializer

class PassengerScheduleView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
# Create your views here.

class UserUpdateView(generics.RetrieveUpdateAPIView):
    
    queryset = CustomUser.objects.filter()
    serializer_class = UpdateUserSerializer

class ChangePasswordView(generics.RetrieveUpdateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = ChangePasswordSerializer