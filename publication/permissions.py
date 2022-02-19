from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import *
from institutions.models import Institution


class IsStorageAllowed(BasePermission):
    message = "Sorry the storage for your institution is currently full please subscribe to another plan"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        # breakpoint()
        if request.data['recommendation'] is not None:
            recommendation = Recommendation.objects.get(
                pk=request.data['recommendation'])
            file = recommendation.file.pdf
            institution = recommendation.institution
            print(file)
            # breakpoint()

            fileAddedSize = institution.storageUsed + file.size

            # breakpoint()

            if fileAddedSize <= institution.storageLimit:
                return True
            return False
        return True
