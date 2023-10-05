from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Order
from ..serializers import OrderSerializer
from django.utils import timezone


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        now_time = timezone.now()
        order_objs = Order.objects.filter()
        return Response({})

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer