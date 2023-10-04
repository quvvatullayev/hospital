from rest_framework import serializers
from .models import Hospital

class HospitalSerializers(serializers.ModelField):
    class Meta:
        model = Hospital
        fields = "__all__"