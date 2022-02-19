from django.urls import path
from .views import *

app_name = 'publication'

urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view(),
         name='Article-detailcreate'),
    path('', ArticleList.as_view(), name='Article-listcreate'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='Review-detailcreate'),
    path('reviews', ReviewList.as_view(), name='Review-listcreate'),

]
