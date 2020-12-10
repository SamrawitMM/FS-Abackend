from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import TripHistory, Owner
from .serializers import TripHistorySerializer, OwnerRegisterSerializer


class TripHistoryView(viewsets.ModelViewSet):
    queryset = TripHistory.objects.all()
    serializer_class = TripHistorySerializer

class OwnerCreateView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerRegisterSerializer