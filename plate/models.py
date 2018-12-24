from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicle_plate(models.Model):
    plate_nubmer = models.CharField(max_length=30, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='created_by')
    user_link = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_link')

    def __str__(self):
        return self.plate_nubmer
