from django.urls import path
from .views import *

app_name = 'transactions'

urlpatterns = [
    path('<int:pk>/', TransactionDetail.as_view(), name='Transaction-detailcreate'),
    path('', TransactionList.as_view(), name='Transaction-listcreate'),
    path('plans', SubscriptionPlanList.as_view(), name='plan-list'),
]