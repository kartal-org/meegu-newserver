from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [   
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('dashboard/', views.home, name="dashboard"),
    
    path('account/', views.account, name="account"), 
    path('accounts_staff/', views.accountStaff, name="accounts_staff"),
    path('accounts_add/', views.accountAdd, name="accounts_add"),
    path('accounts_delete_confirm/<str:pk>/', views.accountDelete, name="accounts_delete_confirm"),
    path('accounts_update/<str:pk>/', views.accountUpdate, name="accounts_update"),
    
    path('classroom/', views.classroom, name="classroom"),
    path('classrooms_delete_confirm/<str:pk>/', views.classroomDelete, name="classrooms_delete_confirm"),
    
    path('institution/', views.institution, name="institution"),
    path('institutions_approved/', views.institutionApproved, name="institutions_approved"),
    path('institutions_disapproved/', views.institutionDisapproved, name="institutions_disapproved"),
    path('institutions_view_verify/<str:pk>/', views.institutionVerify, name="institutions_view_verify"),
    path('institutions_delete_confirm/<str:pk>/', views.institutionDelete, name="institutions_delete_confirm"),
    
    path('subscription/', views.subscription, name="subscription"), 
    path('subscriptions_add/', views.subscriptionAdd, name="subscriptions_add"),
    path('subscriptions_delete_confirm/<str:pk>/', views.subscriptionDelete, name="subscriptions_delete_confirm"), 
    path('subscriptions_update/<str:pk>/', views.subscriptionUpdate, name="subscriptions_update"),
    path('transaction/', views.transaction, name="transaction"),

    path('publication/', views.publication, name="publication"),
    path('publication_delete_confirm/<str:pk>/', views.publicationDelete, name="publications_delete_confirm"),

    path('staff_dashboard/', views.staffhome, name="staffDashboard"),
    path('staff_institution_pending/', views.staffInstitutionPending, name="staffInstitutionPending"),
    path('staff_institution_approved/', views.staffInstitutionApproved, name="staffInstitutionApproved"),
    path('staff_institution_disapproved/', views.staffInstitutionDisapproved, name="staffInstitutionDisapproved"),
    path('staff_institution_verify/<str:pk>/', views.staffInstitutionVerify, name="staffInstitutionVerify"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 