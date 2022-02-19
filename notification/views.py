from rest_framework import generics, permissions
from .models import *
from .serializers import *


class NotificationList(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        queryset = Notification.unread.all()

        user = self.request.user
        history = self.request.query_params.get('history')

        if user is not None:
            queryset = queryset.filter(receiver=user)
        if history:
            queryset = Notification.objects.all()

        return queryset


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
