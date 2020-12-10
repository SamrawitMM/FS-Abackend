from django.shortcuts import render

from rest_framework import viewsets,generics
from .models import Notification
from .models import Car, Driver
from .serializers import NotificationSerializer
from .serializers import CarSerializer, DriverSerializer, DriverRegisterSerializer

class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class DriverView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverRegisterSerializer
