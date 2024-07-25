from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer, CustomUserSerializer
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

#class CustomAuthToken(ObtainAuthToken):
    #serializer_class = CustomAuthTokenSerializer
   # def post(self, request, *args, **kwargs):
      #  serializer = self.serializer_class(data=request.data, context={'request': request})
        #serializer.is_valid(raise_exception=True)
        #user = serializer.validated_data['user']
        #token, created = Token.objects.get_or_create(user=user)
        #return Response({
        #    'token': token.key,
          #  'user_id': user.pk,
            #'username': user.username
       # })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(f"email: {email}, Password: {password}")
        user = authenticate(email=email, password=password)
        print(f"Authenticated user: {user}")

        user = authenticate(email=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
        
    def get(self, request):
        return Response({'message': 'Login page'}, status=200)
