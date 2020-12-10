from django.urls import path, include
from . import views
from rest_framework import routers
from .api import PassengerHistory
from .api import DriverDetails


router = routers.DefaultRouter()
router.register('passengerSchedule', views.PassengerScheduleView)
router.register('passenger' , views.PassengerView)
# handle the urls for us like make 
urlpatterns = [
    #path('', include(router.urls))
    # path('admin/', admin.site.urls),
    # path('passenger/', include('passenger.urls'))
     path('<int:pk>', views.PassengerView.as_view()),
     path('register', views.PassengerCreateView.as_view()),
     path('updatelocation/<int:pk>', views.PassengerUpdateLocationView.as_view()),
     path('viewhistory/<int:pk>',PassengerHistory.as_view()),
     path('viewdriverdetails/<int:pk>',DriverDetails.as_view()),
     path('addschedule/', views.PassengerScheduleCreateView.as_view()),
     path('viewschedule/<int:passenger_id>', views.PassengerScheduleView.as_view())
]
