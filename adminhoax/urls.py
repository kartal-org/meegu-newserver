from django.urls import path
from . import views
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   
    path('login/', views.login, name="login"),
    path('dashboard/', views.home, name="dashboard"),
    path('account/', views.account, name="account"),
    path('accounts_delete_confirm/<str:pk>/', views.accountDelete, name="accounts_delete_confirm"),
    path('classroom/', views.classroom, name="classroom"),
    path('classrooms_delete_confirm/<str:pk>/', views.classroomDelete, name="classrooms_delete_confirm"),
    path('institution/', views.institution, name="institution"),
    path('institutions_view_verify/<str:pk>/', views.institutionVerify, name="institutions_view_verify"),
    path('subscription/', views.subscription, name="subscription"), 
    path('subscriptions_add/', views.subscriptionAdd, name="subscriptions_add"),
    path('subscriptions_delete_confirm/<str:pk>/', views.subscriptionDelete, name="subscriptions_delete_confirm"),
    path('transaction/', views.transaction, name="transaction"),
    path('publication/', views.publication, name="publication"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

