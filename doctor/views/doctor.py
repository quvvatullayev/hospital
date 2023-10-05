from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import DoctorModel, Comment
from ..serializers import DoctorSerializers, CommentSerializers
from customer.models import Order

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers

    # def list(self, request, *args, **kwargs):
    #     doctor_objs = DoctorModel.objects.all()
    #     doctors = DoctorSerializers(doctor_objs, many = True)



    #     return Response({"doctors":doctors.data})

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorModel.objects.all()
    serializer_class = DoctorSerializers

    def retrieve(self, request, *args, **kwargs):
        doctor_obj = DoctorModel.objects.get(id = kwargs['pk'])
        doctor = DoctorSerializers(doctor_obj, many = False)

        comment_objs = Comment.objects.filter(doctor = doctor_obj)
        comments = CommentSerializers(comment_objs, many = False)

        return Response({})
        
        
        
