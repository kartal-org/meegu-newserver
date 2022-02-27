from .models import *
from rest_framework import serializers
from institutions.serializers import InstitutionSerializer


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["institution"] = InstitutionSerializer(instance.institution).data
        response["plan"] = SubscriptionPlanSerializer(instance.plan).data
        return response
