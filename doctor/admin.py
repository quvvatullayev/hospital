from django.contrib import admin
from .models import Comment, DoctorModel, Category
from django.contrib.auth.models import Group

admin.site.register([Comment, DoctorModel, Category])
admin.site.unregister([Group])