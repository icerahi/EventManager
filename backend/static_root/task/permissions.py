from rest_framework import permissions
from .models import Task

class IsOwnerOnly(permissions.BasePermission):
    message="Only owner can access!!"
    
#request view level permission
    def has_permission(self, request, view):
        obj = Task.objects.filter(id=view.kwargs.get('id'))
        if obj.exists():
            if obj[0].user == request.user:
                return True

#object level permission
    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True 
    #     if obj.user == request.user:
    #         return True
 