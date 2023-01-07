from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import generics, serializers
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomObtainPairSerializer
User = get_user_model()
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]
    authentication_classes=[]
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer