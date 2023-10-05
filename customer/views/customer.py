from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import CustomerModel, Order
from ..serializers import CustomerModelSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerModelSerializer
    