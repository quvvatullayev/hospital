from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(AbstractUser):
    name = models.CharField(max_length=20)
    description = models.TextField()
    phone = models.CharField(max_length=30)
    job_time_start = models.TimeField()
    job_time_fenish = models.TimeField()
    
    def __str__(self) -> str:
        return self.name
    
class Commint(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    customer = models.ForeignKey()
    description = models.TextField()