from rest_framework import serializers
from .models import *
from institutions.serializers import InstitutionSerializer


class ResourceSerializer(serializers.ModelSerializer):
    pdf = serializers.FileField(required=False)

    class Meta:
        model = Resource
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["institution"] = InstitutionSerializer(instance.institution).data

        return response
