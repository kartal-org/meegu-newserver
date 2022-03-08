from django.core.management.base import BaseCommand
from transactions.models import SubscriptionPlan


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):

        SubscriptionPlan.objects.create(
            name="Institution Basic",
            description="Get your Free 5GB of storage for your institution's publications and resources",
            price=0.00,
            storageLimit=5000000,
        )
        SubscriptionPlan.objects.create(
            name="Institution Upgrade 1",
            description="Get another 5GB of storage for your institution's publications and resources",
            price=50.00,
            storageLimit=5000000,
        )
        SubscriptionPlan.objects.create(
            name="Institution Upgrade 2",
            description="Get another 15GB of storage for your institution's publications and resources",
            price=100.00,
            storageLimit=1500000,
        )
