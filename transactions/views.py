from rest_framework import generics, permissions
from .models import *
from .serializers import *


class SubscriptionPlanList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionPlanSerializer

    def get_queryset(self):
        """
        SubscriptionPlan query Filters
        """
        queryset = SubscriptionPlan.active.all()

        user = self.request.user
        transactions = Transaction.objects.filter(institution__creator = user)

        if transactions is not None:
            if 0 in [o.plan.price for o in transactions]:
                queryset = SubscriptionPlan.active.exclude(price=0)
        
        return queryset


class TransactionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        SubscriptionPlan query Filters
        """
        queryset = Transaction.objects.all()

        user = self.request.user   

        if user is not None:
            queryset = queryset.filter(institution__creator=user)
        
        return queryset

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer