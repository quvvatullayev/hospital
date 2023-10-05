from rest_framework import serializers
from .models import CustomerModel, Order

class CustomerModelSerializers(serializers.ModelField):
    class Meta:
        model = CustomerModel
        fields = '__all__'