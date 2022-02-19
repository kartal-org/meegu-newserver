from os import read
from rest_framework import serializers
from .models import *
from publication.models import Article
from publication.serializers import ArticleSerializer


class LibraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryItem
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["article"] = ArticleSerializer(
            instance.article).data
        return response
