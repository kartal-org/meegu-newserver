from django.urls import path
from .views import *

app_name = 'chats'

urlpatterns = [
    path('<int:pk>/', ConversationDetail.as_view(),
         name='Conversation-detailcreate'),
    path('', ConversationList.as_view(), name='Conversation-listcreate'),
    path('messages/<int:pk>/', MessageDetail.as_view(),
         name='Message-detailcreate'),
    path('messages', MessageList.as_view(), name='Message-listcreate'),

]
