from rest_framework import serializers
from .models import *
from accounts.serializers import AccountSerializer


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["receiver"] = AccountSerializer(instance.receiver).data
        response["sender"] = AccountSerializer(instance.sender).data
        return response
