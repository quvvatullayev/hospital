from rest_framework import serializers
from .models import DoctorModel, Category, Comment
from customer.serializers import OrderSerializer

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):  # O'zgartirish #1
    class Meta:
        model = Comment
        fields = '__all__'

class DoctorSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)  # O'zgartirish #2
    orders = OrderSerializer(many=True, read_only=True)  # O'zgartirish #3
    class Meta:
        model = DoctorModel
        fields = [
            'id', 
            'username', 
            'first_name', 
            'description', 
            'phone', 
            'job_time_start', 
            'job_time_finish', 
            "comments",  # O'zgartirish #2
            'orders'  # O'zgartirish #3
        ]
