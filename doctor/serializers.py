from rest_framework import serializers
from .models import DoctorModel, Category, Comment

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommintSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'