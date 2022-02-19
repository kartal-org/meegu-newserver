from rest_framework import serializers
from .models import *
from accounts.models import Account


class WorkspaceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Workspace


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = File
