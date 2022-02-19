from django.urls import path
from .views import *

app_name = 'notification'

urlpatterns = [
    path('<int:pk>/', NotificationDetail.as_view(),
         name='Notification-detailcreate'),
    path('', NotificationList.as_view(), name='Notification-listcreate'),
]
