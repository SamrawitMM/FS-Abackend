from rest_framework import generics
from rest_framework.response import Response
from .serializers import PassengerSerializer 
from driver.serializers import DriverSerializer 
from .models import Passenger
from driver.models import Driver

class PassengerHistory(generics.ListAPIView):   
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class DriverDetails(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
