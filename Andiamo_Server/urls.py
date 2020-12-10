from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver/',include('driver.urls')),
    path('owner/',include('owner.urls')),
    path('passenger/', include('passenger.urls')),
    path('user/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
