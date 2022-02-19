from rest_framework import generics, permissions
from .models import *
from .serializers import *


class InstitutionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InstitutionSerializer

    def get_queryset(self):
        """
        Institution query Filters
        """

        user = self.request.user
        verification = self.request.query_params.get('is_verified')
        isActive = self.request.query_params.get('isActive')

        queryset = Institution.active.all()

        if user is not None:
            queryset = queryset.filter(creator=user)
        if verification is not None:
            queryset = queryset.filter(is_verified=verification)
        if isActive is not None:
            queryset = Institution.objects.filter(isActive=False)

        return queryset


class InstitutionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class DepartmentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        """
        Department query Filters
        """

        institution = self.request.query_params.get('institution')
        archive = self.request.query_params.get('archive')

        queryset = Department.active.all()

        if institution is not None:
            queryset = queryset.filter(institution=institution)
        if archive:
            queryset = Department.objects.filter(isActive=False)

        return queryset


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class MemberList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MemberSerializer

    def get_queryset(self):
        """
        Member query Filters
        """

        institution = self.request.query_params.get('institution')
        isActive = self.request.query_params.get('isActive')

        queryset = Member.active.all()

        if institution is not None:
            queryset = queryset.filter(institution=institution)
        if isActive is not None:
            queryset = Member.objects.filter(isActive=False)

        return queryset


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class VerificationCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VerificationSerializer
