# from rest_framework import serializers
# from .models import Notification
# from .models import Car

# #this is serializer
# class NotificationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Notification
#         # fields = ('url','id','case','reason')
#         fields = '__all__'
        
# class CarSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Car
#         # fields = ('url','id','license_plate','num_of_seats','car_model')
#         fields = '__all__'

from rest_framework import serializers
from .models import Notification
from .models import Car, Driver
from users.serializers import UserSerializer
from users.models import CustomUser

class DriverRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Driver
        fields = ['user']

    def create(self,validated_data):
        # print(validated_data)
        user_data = validated_data.pop('user')
        password = user_data['password']
        user = CustomUser.objects.create(**user_data,user_type = 1,is_active=False)
        user.set_password(password)
        user.save()
        driver = Driver.objects.create(user=user,**validated_data)
        return driver 

class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Driver
        fields = '__all__'

    def create(self,validated_data):
        # print(validated_data)
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data,user_type = 1,is_active=False)
        driver = Driver.objects.create(user=user,**validated_data)
        return driver 

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ('url','id','case','reason')

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('url','id','license_plate','num_of_seats','car_model')

