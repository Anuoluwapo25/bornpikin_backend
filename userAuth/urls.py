from django.urls import path
from .views import RegisterView, LoginView, BookingView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    #path('login/', CustomAuthToken.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('booking/',BookingView.as_view(), name='booking'),
    # path('booking-history/', BookingHistoryView.as_view(), name='booking-history'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
