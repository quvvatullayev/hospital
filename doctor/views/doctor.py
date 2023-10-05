from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import DoctorModel, Comment
from ..serializers import DoctorSerializers, CommintSerializers

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers

    def retrieve(self, request, *args, **kwargs):
        doctor_obj = DoctorModel.objects.get(id = kwargs['pk'])
        doctor = DoctorSerializers(doctor_obj, many = False)

        comment_objs = Comment.objects.filter(doctor = doctor_obj)
        comments = CommintSerializers(comment_objs, many = False)

        return Response({})
        
        
        
