from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import HospitalSerializers, Hospital

class HospitalListCreateView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializers

class HospitalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializers