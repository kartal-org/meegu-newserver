from .models import *
from rest_framework import serializers
from institutions.serializers import InstitutionSerializer, DepartmentSerializer
from classrooms.serializers import RecommendationSerializer
from accounts.serializers import AccountSerializer


class ArticleSerializer(serializers.ModelSerializer):
    pdf = serializers.FileField()

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "abstract",
            "rating",
            "dateCreated",
            "pdf",
            "dateUpdated",
            "institution",
            "citation",
            "recommendation",
            "department",
            "status",
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["department"] = DepartmentSerializer(instance.department).data
        return response

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["institution"] = InstitutionSerializer(instance.institution).data
        return response

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["recommendation"] = RecommendationSerializer(instance.recommendation).data
        return response


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = AccountSerializer(instance.user).data
        return response
