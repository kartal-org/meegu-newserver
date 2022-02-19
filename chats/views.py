from rest_framework import generics, permissions, status, response
from .models import *
from .serializers import *


class ConversationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer

    def get_queryset(self):
        user = self.request.user
        archive = self.request.query_params.get('archive')
        queryset = Conversation.active.all()
        if user is not None:
            queryset = queryset.filter(members__in=[user.id, ])
        if archive:
            queryset = Conversation.objects.all()
        return queryset


class ConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class MessageList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        convo = self.request.query_params.get('convo')
        archive = self.request.query_params.get('archive')
        queryset = Message.active.all()
        if convo is not None:
            queryset = queryset.filter(conversation__id=convo)
        if archive:
            queryset = Message.objects.all()
        return queryset


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
