from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img = models.ImageField(upload_to='./category_img')

    def __str__(self):
        return self.title

class DoctorModel(AbstractBaseUser):
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    description = models.TextField()
    phone = models.CharField(max_length=30)
    job_time_start = models.TimeField()
    job_time_finish = models.TimeField()
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    doctor = models.ForeignKey('DoctorModel', on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.CustomerModel', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.customer.name
