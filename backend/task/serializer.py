from rest_framework.serializers import ModelSerializer
from .models import Task
from rest_framework import serializers

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']
   
        

        
    # def validate(self, attrs):
    #     attrs['user']=self.context['request'].user
    #     return super().validate(attrs)
        