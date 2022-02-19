from django.urls import path
from .views import *

app_name = 'workspaces'

urlpatterns = [
    path('<int:pk>/', WorkspaceDetail.as_view(), name='workspace-detailcreate'),
    path('', WorkspaceList.as_view(), name='workspace-listcreate'),
    path('files/<int:pk>/', FileDetail.as_view(), name='file-detailcreate'),
    path('files', FileList.as_view(), name='file-listcreate'),
    
]