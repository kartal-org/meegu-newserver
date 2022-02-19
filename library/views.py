from rest_framework import generics, permissions, status, response
from .models import *
from .serializers import *


class LibraryItemList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LibraryItemSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = LibraryItem.objects.all()
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset


class LibraryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
