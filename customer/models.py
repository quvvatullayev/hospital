from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomerModel(AbstractBaseUser):
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey('CustomerModel', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.DoctorModel', on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.doctor.name} | {self.customer.name}"
