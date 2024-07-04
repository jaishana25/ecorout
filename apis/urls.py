from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import *

urlpatterns = [
    path("trips/", TripsListAPIView.as_view()),
    path('eco-bot/', SustainableTravelChatView.as_view(), name='Eco-Bot'),

    #authentication
    path('register/', RegisterUserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
]