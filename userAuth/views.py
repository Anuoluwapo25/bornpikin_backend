from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.utils import timezone
from .serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer, BookUserSerializer
from .models import CustomUser, BookUser

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
    

class BookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        data['name'] = request.user.id

        serializer = BookUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # booking = serializer.save(user=request.user)
            # return Response({
            #     'booking': serializer.data,
            #     'message': 'Booking confirmed!',
            #     'appointment': {
            #         'service': booking.services,
            #         'dentist': booking.dentist,
            #         'date': booking.date,
            #         'time': booking.time,
            #     }
            # }, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        # Get upcoming bookings
        upcoming_bookings = BookUser.objects.filter(
            name=request.user,
            date__gte=timezone.now().date(),
            is_completed=False
        ).order_by('date', 'time')
        serializer = BookUserSerializer(upcoming_bookings, many=True)
        return Response(serializer.data)

# User Profile View
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,  # Add custom fields if necessary
            'location': user.location,          # Add custom fields if necessary
            # Add any other fields you want to include from the CustomUser model
        }
        return Response(data, status=status.HTTP_200_OK)


# class BookingHistoryView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         # Get booking history
#         history = BookUser.objects.filter(
#             name=request.user,
#             is_completed=True
#         ).order_by('-date', '-time')
#         serializer = BookUserSerializer(history, many=True)
#         return Response(serializer.data)

