from rest_framework import serializers
from .models import Doctor, Category, Commint

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommintSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commint
        fields = '__all__'