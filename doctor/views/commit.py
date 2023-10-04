from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Commint, CommintSerializers

class CommintListCreateView(generics.ListCreateAPIView):
    queryset = Commint.objects.all()
    serializer_class = CommintSerializers
    