from rest_framework import serializers
from .models import *
from accounts.serializers import AccountSerializer
from workspaces.serializers import FileSerializer
from institutions.serializers import InstitutionSerializer


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["file"] = FileSerializer(instance.file).data
        response["adviser"] = AccountSerializer(instance.adviser).data
        response["institution"] = InstitutionSerializer(instance.institution).data

        return response


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"

    pass


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment

        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["author"] = AccountSerializer(instance.author).data

        return response
