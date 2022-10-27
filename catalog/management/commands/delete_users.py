from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']
        if User.objects.filter(id__in=users_ids, is_superuser=1).exists():
            self.stdout.write('Superuser cant be deleted!')
        else:
            User.objects.filter(id__in=users_ids).delete()
            self.stdout.write('Users are deleted!')

    # def handle(self, *args, **kwargs):
    #     users_ids = kwargs['user_id']
    #     q = 0
    #     try:
    #         for i in users_ids:
    #             user = User.objects.get(pk=i)
    #             if user.is_superuser:
    #                 q += 1
    #         if q > 0:
    #             self.stdout.write('Superuser cant be deleted!')
    #         else:
    #             for user_id in users_ids:
    #                 user = User.objects.get(pk=user_id)
    #                 user.delete()
    #                 self.stdout.write('User "%s (%s)" deleted with success!' % (user.username, user_id))
    #     except User.DoesNotExist:
    #         self.stdout.write('User does not exist.')
