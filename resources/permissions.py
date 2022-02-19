from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.db.models import Sum, IntegerField
from .models import *
from institutions.models import Institution


class IsStorageAllowed(BasePermission):
    message = "Sorry the storage for your institution is currently full please subscribe to another plan"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        file = request.data.get('pdf')
        # breakpoint()

        if file == None:
            return True
        institution = Institution.objects.get(
            pk=request.data.get('institution'))
        fileAddedSize = institution.storageUsed + file.size
        # breakpoint()

        if fileAddedSize <= institution.storageLimit:
            return True
        return False
