from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework import status
from .models import Account
from .serializers import AccountSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import filters
from django.db.models import Q
from .renderers import CustomRenderer


class AccountList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        queryset = Account.objects.all()
        type = self.request.query_params.get("type")
        name = self.request.query_params.get("name")

        if name is not None:
            queryset = queryset.filter((Q(first_name__icontains=name) | Q(last_name__icontains=name)))
        if type is not None:
            queryset = queryset.filter(type=type)
        return queryset


class AccountDetail(generics.RetrieveUpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class MyProfileView(generics.RetrieveAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.request.user.pk)
        return obj
