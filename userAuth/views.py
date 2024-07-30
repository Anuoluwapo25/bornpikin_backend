from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer
from .models import CustomUser

# Register View
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'user': CustomUserSerializer(user).data,
                    'token': token.key
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({'message': 'Please use POST to register a new user'}, status=status.HTTP_200_OK)

# Login View
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        return Response({'message': 'Please use POST to login'}, status=status.HTTP_200_OK)