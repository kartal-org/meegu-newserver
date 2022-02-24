from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from accounts.models import Account
from institutions.models import Institution, Department, Member
import random
from django.contrib.auth import authenticate, login

USERS = Account.objects.all().filter(type="adviser")
DEPARTMENTS = [
    "College of Arts and Sciences",
    "College of Engineering",
    "College of Business",
    "College of Fine Arts and Communication",
    "College of Education",
]


class Provider(faker.providers.BaseProvider):
    def users(self):
        return self.random_element(USERS)

    def departments(self):
        return self.random_element(DEPARTMENTS)


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):

        fake = Faker(["en_US"])
        fake.add_provider(Provider)

        for _ in USERS:
            name = fake.unique.first_name()
            contact = fake.unique.last_name()
            address = fake.address()
            email = "%s@example.org" % (name)
            about = fake.sentence()
            creator = fake.users()

            Institution.objects.create_user(
                name=name, contact=contact, address=address, email=email, about=about, creator=creator
            )
            print(name, creator)

            department = fake.unique.departments()

            Department.objects.create_user(name=department, institution=name)
            print(department, name)

            member = creator

            Member.objects.create_user(user=member, instance=name)
            print(member, name)
