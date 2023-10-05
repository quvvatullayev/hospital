from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Comment, CommentSerializers

class CommintListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

class CommintRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

