from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers




urlpatterns = [
   #   path('<int:pk>', views.PassengerView.as_view()),
     path('register', views.OwnerCreateView.as_view()),
   #   path('updatelocation/<int:pk>', views.PassengerUpdateLocationView.as_view()),
   #   path('viewhistory/<int:pk>',PassengerHistory.as_view()),
   #   path('viewdriverdetails/<int:pk>',DriverDetails.as_view()),
   #   path('addschedule/', views.PassengerScheduleCreateView.as_view()),
   #   path('viewschedule/<int:passenger_id>', views.PassengerScheduleView.as_view())

]
