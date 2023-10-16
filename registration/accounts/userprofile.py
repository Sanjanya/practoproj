from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    userID = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=[('doctor', 'Doctor'), ('patient', 'Patient')])