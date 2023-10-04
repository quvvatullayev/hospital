from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Doctor
from ..serializers import DoctorSerializers

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
