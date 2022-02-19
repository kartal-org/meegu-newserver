from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):

    profileImage = serializers.FileField()
    profileCover = serializers.FileField()

    class Meta:
        model = Account
        exclude = ('password', 'groups', 'user_permissions',)

    def validate_email(self, value):
        user = self.context["request"].user
        if Account.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if Account.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": "This username is already in use."})
        return value
