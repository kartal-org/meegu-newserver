from django.forms import ModelForm 
import datetime
from .models import *
from accounts.models import *
from transactions.models import *
from classrooms.models import *
from institutions.models import Institution, Department, Verification

class InstitutionVerifyForm(ModelForm):
	class Meta:
		model = Verification
		fields = ['status']

class AddSubscriptionPlan(ModelForm):
	class Meta:
		model = SubscriptionPlan
		fields = '__all__'