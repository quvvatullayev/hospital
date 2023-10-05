from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img = models.ImageField(upload_to='./category_img')

    def __str__(self):
        return self.title

class DoctorModel(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)  # USERNAME_FIELD ni qo'shing
    first_name = models.CharField(max_length=20)
    description = models.TextField()
    phone = models.CharField(max_length=30)
    job_time_start = models.TimeField()
    job_time_finish = models.TimeField()
    
    # USERNAME_FIELD ni sozlang
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
class Comment(models.Model):
    doctor = models.ForeignKey('DoctorModel', on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.CustomerModel', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.customer.username
