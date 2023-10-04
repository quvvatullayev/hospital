from django.contrib import admin
from .models import Commint, Doctor, Category
from django.contrib.auth.models import Group

admin.site.register([Commint, Doctor, Category])
admin.site.unregister([Group])