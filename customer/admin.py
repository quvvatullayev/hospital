from django.contrib import admin
from .models import CustomerModel, Order

admin.site.register([CustomerModel, Order])
