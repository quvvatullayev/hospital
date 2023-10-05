from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import DoctorModel
from ..serializers import DoctorSerializers

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers
