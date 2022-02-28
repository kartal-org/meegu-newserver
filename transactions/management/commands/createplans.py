from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from transactions.models import SubscriptionPlan
import random
import decimal
from django.contrib.auth import authenticate, login
 
class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):

        fake = Faker(["tl_PH"])  
        SubscriptionPlan.objects.create(
            name="Institution Basic", 
            description="Free One Time Subscription Plan For Institution.", 
            price=50.00,
            storageLimit=10000000000,
        )
        SubscriptionPlan.objects.create(
            name="Institution Upgrade 1",
            description="Extend 5GB to your Institution Storage",
            price=50.00,
            storageLimit=10000000000,
        )
        SubscriptionPlan.objects.create(
            name="Institution Upgrade 2",
            description="Extend 5GB to your Institution Storage",
            price=50.00, 
            storageLimit=10000000000,
        ) 