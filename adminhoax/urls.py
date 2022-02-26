from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib.auth import views as auth_views
# from django.conf.urls import url

urlpatterns = [
    # url(r'^login/$', auth_views.login, {'loginPage': 'adminhoax/login.html'}, name='login'),
    # url(r'^login/$', auth_views.login, name='login'),
    path("login/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logoutUser"),
    path("dashboard/", views.home, name="dashboard"),
    path("account/", views.account, name="account"),
    path("accounts_staff/", views.accountStaff, name="accounts_staff"),
    path("accounts_add/", views.accountAdd, name="accounts_add"),
    path("accounts_delete_confirm/<str:pk>/", views.accountDelete, name="accounts_delete_confirm"),
    path("accounts_update/<str:pk>/", views.accountUpdate, name="accounts_update"),
    path("classroom/", views.classroom, name="classroom"),
    path("classrooms_delete_confirm/<str:pk>/", views.classroomDelete, name="classrooms_delete_confirm"),
    path("institution/", views.institution, name="institution"),
    # path('institution/', views.institutionPending, name="institution"),
    path("institutions_approved/", views.institutionApproved, name="institutions_approved"),
    path("institutions_view_verify/<str:pk>/", views.institutionVerify, name="institutions_view_verify"),
    path("institutions_delete_confirm/<str:pk>/", views.institutionDelete, name="institutions_delete_confirm"),
    path("subscription/", views.subscription, name="subscription"),
    path("subscriptions_add/", views.subscriptionAdd, name="subscriptions_add"),
    path("subscriptions_delete_confirm/<str:pk>/", views.subscriptionDelete, name="subscriptions_delete_confirm"),
    path("subscriptions_update/<str:pk>/", views.subscriptionUpdate, name="subscriptions_update"),
    path("transaction/", views.transaction, name="transaction"),
    path("publication/", views.publication, name="publication"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
