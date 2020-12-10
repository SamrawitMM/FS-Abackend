from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url
urlpatterns = [
    # path('', views.PassengerCreateView.as_view()),
    path('update/<int:pk>', views.UserUpdateView.as_view()),
    path('changepassword/<int:pk>', views.ChangePasswordView.as_view())


    # url(r'^rest-auth/', include('rest_auth.urls')),

]