from rest_framework import serializers
from .models import CustomerModel, Order

class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
