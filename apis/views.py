from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .services import *


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'Registration successful and user logged in'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Registration successful but login failed'}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class TripsListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        try:
            profile = Profile.objects.get(user = request.user)
        except Profile.DoesNotExist:
            return Response({"error":"User Doesn't exist"},status= status.HTTP_404_NOT_FOUND)
        
        trips = Trips.objects.filter(profile = profile)
        serializer = TripSerializer(trips, many = True)
        
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request, format = None):

        try:
            profile = Profile.objects.get(user = request.user)
        except Profile.DoesNotExist:
            return Response({"error":"Profile Doesn't exist"},status= status.HTTP_404_NOT_FOUND)
        
        serializer = TripSerializer(date = request.data)
        if serializer.is_valid():
            serializer.save(profile = profile)

            return Response({"message": "Trip created successfully"}, status= status.HTTP_200_OK)
        
        return Response({"errors": serializer.errors}, status= status.HTTP_400_BAD_REQUEST)


class SustainableTravelChatView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user_input = request.data.get('message')
        if not user_input:
            return Response({"error": "Message content is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        response = get_sustainable_travel_response(user_input)
        return Response({"response": response}, status=status.HTTP_200_OK)
