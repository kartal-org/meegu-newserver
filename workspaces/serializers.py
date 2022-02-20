from rest_framework import serializers
from .models import *
from accounts.models import Account
from accounts.serializers import AccountSerializer


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Workspace

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.adviser is not None:
            response["adviser"] = AccountSerializer(instance.adviser).data

        if instance.members is not None:
            memberIDs = instance.members
            members = []

            for x in memberIDs.all():
                members.append(AccountSerializer(x).data)
            response["members"] = members

        response["creator"] = AccountSerializer(instance.creator).data

        return response


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = File
