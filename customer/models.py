from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone


class CustomerModel(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    
    
    def __str__(self):
        return self.username
    
class Order(models.Model):
    customer = models.ForeignKey('CustomerModel', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.DoctorModel', on_delete=models.CASCADE)
    time = models.DateTimeField()
    is_expired = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Har bir yangi Order obyektini saqlashda vaqtni solishtirib, is_expired ni yangilaymiz
        current_time = timezone.now()
        if self.time < current_time:
            self.is_expired = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.doctor.username} | {self.customer.username}"
