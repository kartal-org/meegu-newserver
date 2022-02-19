from rest_framework import serializers
from .models import *


class ResourceSerializer(serializers.ModelSerializer):
    pdf = serializers.FileField(required=False)

    class Meta:
        model = Resource
        fields = '__all__'
