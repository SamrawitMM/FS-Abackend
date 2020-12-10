from rest_framework import serializers
from .models import PassengerSchedule ,Passenger
# from .models import Passenger
from users.serializers import UserSerializer
from users.models import CustomUser
class PassengerScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerSchedule
        fields = '__all__'

# class PassengerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Passenger
#         fields = ('id', 'name')
class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Passenger
        fields = '__all__'

    def create(self,validated_data):
        # print(validated_data)
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data,user_type = 2)
        passenger = Passenger.objects.create(user=user,**validated_data)
        return passenger 

class UpdatePassengerLocationSerializer(serializers.ModelSerializer):
    # user = UpdateUserSerializer()

    class Meta:
        model = Passenger 
        exclude = ['user']


class PassengerRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, partial=True)
    class Meta:
        model=Passenger
        fields = ['user']

    def create(self,validated_data):
        # print(validated_data)
        user_data = validated_data.pop('user')
        password = user_data['password']
        user = CustomUser.objects.create(**user_data,user_type = 2)
        user.set_password(password)
        user.save()
        passenger = Passenger.objects.create(user=user,**validated_data)
        return passenger 

# class PassengerUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [
#             'username',
#             'password',
#         ]

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username',instance.username)
#         print('instance of username',instance.username)
#         return instance 
    # def update(self,instance,validated_data,partial = True):
    #     print('this is working')
    #     # user_data = validated_data.pop('user')
    #     # user_serializer = UserSerializer(partial = True)
    #     # super(self.__class__, self).update(instance,validated_data)
    #     # super(UserSerializer,user_serializer).update(instance.user,user_data)
    #     return instance