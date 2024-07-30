from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    location = serializers.CharField()

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError({'error': 'Invalid credentials'})

        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    location = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            location=validated_data['location'],
            password=validated_data['password']
        )
        return user

    # def validate_email(self, value):
    #     if CustomUser.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("A user with this email already exists.")
    #     return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

# class RegisterSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     name = serializers.CharField()
#     email = serializers.EmailField()
#     phone_number = serializers.CharField()
#     location = serializers.CharField()

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             name=validated_data['name'],
#             email=validated_data['email'],
#             phone_number=validated_data['phone_number'],
#             location=validated_data['location']
#         )
#         return user

# def retrieve(self, request, pk=None):
#     user = CustomUser.objects.get(pk=pk)
#     serializer = CustomUserSerializer(user)
#     return Response(serializer.data)