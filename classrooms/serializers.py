from rest_framework import serializers
from .models import *


class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'

    pass


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
