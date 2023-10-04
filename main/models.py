from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField('./hospital_imgs')
    description = models.TextField()
    location = models.CharField(max_length=225)
    phone = models.CharField(max_length=30)
    start_time = models.TimeField()
    finesh_time = models.TimeField()

    def __str__(self) -> str:
        return self.name