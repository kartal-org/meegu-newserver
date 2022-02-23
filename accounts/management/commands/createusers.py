from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from accounts.models import Account
import random
from django.contrib.auth import authenticate, login

TYPE = [
    ("moderator", "Moderator"),
    ("adviser", "Adviser"),
    ("researcher", "Researcher"),
]

class Provider(faker.providers.BaseProvider):
    def type(self):
        return self.random_element(TYPE)

class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):

        fake = Faker(["en_US"]) 
        fake.add_provider(Provider)
 
        for _ in range(5):
            fname = fake.unique.first_name()
            lname = fake.unique.last_name()
            uname = "%s%s%d" % (fname.lower(), lname.lower(), random.randint(1000, 9999))
            email = "%s@example.org" % (uname) 
            password = "QaxSf96H"
            about = fake.sentence()
            type = fake.type()

            Account.objects.create_user(
                first_name=fname, last_name=lname, username=uname, email=email, password=password, about=about, type=type
            )
            print(email, password)

