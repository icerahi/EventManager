from django.db import models
from django.conf import settings
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    note = models.CharField(max_length=300)
    color = models.CharField(max_length=20,default='whitesmoke')
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.note}'
    class Meta:
        ordering = ('-created',)