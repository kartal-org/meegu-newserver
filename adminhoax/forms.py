from django.forms import ModelForm
import datetime
from .models import *
from accounts.models import *
from transactions.models import *
from classrooms.models import *
from institutions.models import Institution, Department, Verification
from django.contrib.auth.forms import UserCreationForm


class InstitutionVerifyForm(ModelForm):
    class Meta:
        model = Verification
        fields = ["status"]


class UpdateAccount(ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "username", "email", "is_active"]


class AddStaffAccount(UserCreationForm):
    class Meta:
        model = Account
        #fields = '__all__'
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "is_staff"]


class AddSubscriptionPlan(ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"


class UpdateSubscriptionPlan(ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = "__all__"
