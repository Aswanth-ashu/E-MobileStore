from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from models import APIKey
import secrets
import string

class Command(BaseCommand):
    help = 'Generate API keys for users'

    def handle(self, *args, **options):
        for user in User.objects.all():
            if not user.api_keys.exists():
                api_key = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(32))
                APIKey.objects.create(user=user, key=api_key)
                self.stdout.write(self.style.SUCCESS(f'API key created for {user.username}'))