from django.shortcuts import render
from rest_framework import viewsets,generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PassengerSchedule , Passenger
from rest_framework.mixins import UpdateModelMixin
from .serializers import PassengerScheduleSerializer ,PassengerSerializer, PassengerRegisterSerializer,UpdatePassengerLocationSerializer
from django.conf import settings
# from .serializers import PassengerSerializer
# from .models import Passenger

from users.serializers import UserSerializer
class PassengerScheduleUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PassengerSchedule.objects.all()
    serializer_class = PassengerScheduleSerializer

class PassengerScheduleCreateView(generics.CreateAPIView):
    queryset = PassengerSchedule.objects.all()
    serializer_class = PassengerScheduleSerializer

class PassengerScheduleView(generics.ListAPIView):

    queryset = PassengerSchedule.objects.filter()
    serializer_class = PassengerScheduleSerializer
    def get_queryset(self):
        return super().get_queryset().filter(passenger=self.kwargs['passenger_id'])
# class PassengerScheduleView(APIView):
    
    # def get(self,request,pk):
    #     passengerSchedule = PassengerSchedule.objects.filter(passenger=pk)
    #     print(passengerSchedule)
        # serializer = PassengerScheduleSerializer(passengerSchedule)
        # return Response(serializer.data)
    # queryset = PassengerSchedule.objects.all()
    # serializer_class = PassengerScheduleSerializer

# class PassengerUpdateView(generics.RetrieveUpdateAPIView,UpdateModelMixin):
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer
    
#     def put(self, request, *args, **kwargs):
#         print('please be here')
#         return self.partial_update(request, *args, **kwargs)

class PassengerUpdateLocationView(generics.RetrieveUpdateAPIView):

    queryset = Passenger.objects.filter()
    serializer_class = UpdatePassengerLocationSerializer

class PassengerCreateView(generics.CreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerRegisterSerializer

class PassengerView(generics.ListAPIView):
    queryset = Passenger.objects.filter()
    serializer_class = PassengerSerializer