from rest_framework import serializers
from .models import *


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class VerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verification
        fields = '__all__'
