from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'email', 'phone_number', 'location']
        read_only_fields = ['id', 'username']
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'name', 'email', 'phone_number', 'location']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            location=validated_data['location']
        )
        return user

