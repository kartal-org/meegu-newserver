from django.urls import path
from .views import *

app_name = 'workspaces'

urlpatterns = [
    path('<int:pk>/', RecommendationDetail.as_view(), name='Recommendation-detailcreate'),
    path('', RecommendationList.as_view(), name='Recommendation-listcreate'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detailcreate'),
    path('comments', CommentList.as_view(), name='comment-listcreate'),
    path('replies/<int:pk>/', ReplyDetail.as_view(), name='reply-detailcreate'),
    path('replies', ReplyList.as_view(), name='reply-listcreate'),
    
]