from django.db import models
from django.shortcuts import render
from rest_framework import generics
from .serializer import TaskSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from .models import Task
from .permissions import IsOwnerOnly

# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query')

        if query == 'done':
            return super().get_queryset().filter(user=self.request.user).filter(is_done=True)
        elif query == 'undone':
            return super().get_queryset().filter(user=self.request.user).filter(is_done=False)

        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class TaskUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOnly, ]

    lookup_field = 'id'
