from django.urls import path
from .views import *

app_name = 'institutions'

urlpatterns = [
    path('<int:pk>/', InstitutionDetail.as_view(), name='Institution-detailcreate'),
    path('', InstitutionList.as_view(), name='Institution-listcreate'),
    path('departments/<int:pk>/', DepartmentDetail.as_view(), name='Department-detailcreate'),
    path('departments', DepartmentList.as_view(), name='Department-listcreate'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='Member-detailcreate'),
    path('members', MemberList.as_view(), name='Member-listcreate'),
    path('verification', VerificationCreate.as_view(), name='Verification-create'),
    
]