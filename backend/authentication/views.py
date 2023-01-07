from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import generics, serializers,permissions,response,status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomObtainPairSerializer
from .serializers import ChangePasswordSerializer
User = get_user_model()
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]
    authentication_classes=[]
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class=ChangePasswordSerializer
    model=User
    permission_classes=(permissions.IsAuthenticated,)

    def get_object(self):
        obj=self.request.user 
        return obj 

    def update(self,request,*args,**kwargs):
        self.object=self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return response.Response({'old_password':['Wrong password']},status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return response.Response({'message':'Password updated successfully'},status=status.HTTP_200_OK)