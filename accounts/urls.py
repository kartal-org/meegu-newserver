from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('<int:pk>/', AccountDetail.as_view(), name='detailview'),
    path('', AccountList.as_view(), name='listcreate'),
    path('me', MyProfileView.as_view(), name='my-profile'),
]
