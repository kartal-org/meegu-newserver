from rest_framework import serializers
from .models import *
from accounts.serializers import AccountSerializer
from accounts.models import Account


class ConversationSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(slug_field="username", many=True, queryset=Account.objects.all())

    class Meta:
        model = Conversation
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.members is not None:
            memberIDs = instance.members
            members = []

            for x in memberIDs.all():
                members.append(AccountSerializer(x).data)
            response["members"] = members

        return response


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["sender"] = AccountSerializer(instance.sender).data
        response["receiver"] = AccountSerializer(instance.receiver).data

        return response
