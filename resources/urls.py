from django.urls import path
from .views import *

app_name = 'resources'

urlpatterns = [
    path('<int:pk>/', ResourceDetail.as_view(), name='Resource-detailcreate'),
    path('', ResourceList.as_view(), name='Resource-listcreate'),
    path('import', ImportResource.as_view(), name='Resource-import'),
]
