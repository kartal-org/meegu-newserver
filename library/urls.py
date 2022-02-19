from django.urls import path
from .views import *

app_name = 'library'

urlpatterns = [
    path('<int:pk>/', LibraryItemDetail.as_view(),
         name='LibraryItem-detailcreate'),
    path('', LibraryItemList.as_view(), name='LibraryItem-listcreate'),
]
