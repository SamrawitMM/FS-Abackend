# from django.urls import path, include
# from .import views
# from rest_framework import routers
# #urls
# router = routers.DefaultRouter()
# router.register('Car',views.CarView)
# router.register('Notification',views.NotificationView),

# urlpatterns = [
#     path('', include(router.urls))
# ]
from django.urls import path, include
from .import views
# from .api import CarCreateApi
# from .api import CarUpdateApi
# from .api import CarApi
# from .api import CarDeleteApi
from rest_framework import routers
from django.conf.urls import url

#urls
# router = routers.DefaultRouter()
# router.register('Car',views.CarView)
# router.register('Notification',views.NotificationView),
# router.register('Driver',views.DriverView),

urlpatterns = [
    # path('', include(router.urls))
    # path('registerdriver',)
    path('register', views.DriverCreateView.as_view()),
     path('<int:pk>', views.DriverView.as_view()),
    # path('api',CarApi.as_view()),
    # path('api/create',CarCreateApi.as_view()),
    # path('api/<int:pk>',CarUpdateApi.as_view()),
    # path('api/<int:pk>/delete',CarDeleteApi.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),

]