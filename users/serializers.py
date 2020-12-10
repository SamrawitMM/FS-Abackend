from django.conf import settings
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField( style={'input_type': 'password', 'placeholder': 'Password'}, write_only= True,required=True)
    password2 = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Confirm Password'},label='Confirm Password', write_only= True)
    class Meta:
        model=CustomUser
        exclude = ['date_joined','last_login','is_staff','is_active','user_permissions','groups','is_superuser','user_type'] #'Date joined','Groups','User permissions'
        # fields = ['username','email','full_name', 'phone_number','password']
        # exclude = ['Superuser status','Staff status','Date joined','Groups','User permissions']
        # extra_kwargs = {'password': {'write_only': True},'password2': {'write_only': True},}

    def validate_email(self,email):
        existing = CustomUser.objects.filter(email = email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")
        return email

    def validate(self,data):
        if not data.get('password') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        data.pop('password2')
        return data

    def create(self,validated_data):
        # validated_data.pop['password']
        validated_data['password'] = make_password(validated_data.get('password'))
        user = settings.AUTH_USER_MODEL.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        # user = User.objects.create_user(**validated_data)
        
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        exclude = ['date_joined','last_login','is_staff','is_active','user_permissions','groups','is_superuser','user_type','password'] #'Date joined','Groups','User permissions'
        
    def update(self, instance, validated_data):
        # print('this is being run')
        user = super().update(instance, validated_data)
        try:
            # user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance