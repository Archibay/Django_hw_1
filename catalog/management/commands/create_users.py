from itertools import islice

from django.contrib.auth import get_user_model
from django.contrib.auth import hashers
from django.core.management.base import BaseCommand

from faker import Faker


User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11), help='Indicates the number of users to be created')

    def handle(self, **kwargs):
        total = kwargs['total']
        objs = (User(username=fake.name(), email=fake.ascii_email(),
                     password=hashers.make_password(str(fake.password()))) for i in range(total))
        while True:
            batch = list(islice(objs, total))
            if not batch:
                break
            User.objects.bulk_create(batch, total)

        # for i in range(total):
        #     User.objects.create(username=fake.name(), email=fake.ascii_email(), password=fake.password())
