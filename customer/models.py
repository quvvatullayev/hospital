from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Customer(AbstractBaseUser):
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name