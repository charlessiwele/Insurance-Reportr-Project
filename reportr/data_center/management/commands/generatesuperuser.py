import logging
import pathlib
import random
import string
from django.contrib.auth.models import User
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'GENERATE A SUPERUSER'
    """
    This command is useful for generating a superuser with randomly generated username and email detail combo
    The details will be written to a file including the default password
    """

    def handle(self, *args, **options):
        try:
            if options.get('users_dir'):
                users_dir = options.get('users_dir')
            else:
                users_dir = './user_credentials/super_users'
            pathlib.Path(users_dir).mkdir(parents=True, exist_ok=True)
            print('Welcome to custom superuser generator')
            if options.get('username'):
                username = options.get('username')
            else:
                username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            user_email = f'{username}@{username[:4]}.{username[:2]}'

            if options.get('password'):
                password = options.get('password')
            else:
                password = username[:5]

            User.objects.create_superuser(username, user_email, password)
            print(f'username: {username} user_email: {user_email}, password: {password}')
            with (open(f'{users_dir}/{username}.txt', 'w+')) as writer:
                writer.write(f'Super User Credentials')
                writer.write(f'\nusername: {username}')
                writer.write(f'\npassword: {password}')
                writer.write(f'\nuser_email: {user_email}')
        except Exception as exception:
            print(exception.__str__())
