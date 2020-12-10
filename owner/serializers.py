from rest_framework import serializers
from .models import TripHistory, Owner
from users.serializers import UserSerializer
from users.models import CustomUser
class TripHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TripHistory
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model=Owner
        fields = '__all__'

    def create(self,validated_data):
    # print(validated_data)
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data,user_type = 3,is_active=False)
        print(user)
        owner = Owner.objects.create(user=user,**validated_data)
        return owner 

class OwnerRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, partial=True)
    class Meta:
        model= Owner
        fields = ['user']

    def create(self,validated_data):
        # print(validated_data)
        user_data = validated_data.pop('user')
        password = user_data['password']
        user = CustomUser.objects.create(**user_data,user_type = 3,is_active=False)
        user.set_password(password)
        user.save()
        owner = Owner.objects.create(user=user,**validated_data)
        return owner 