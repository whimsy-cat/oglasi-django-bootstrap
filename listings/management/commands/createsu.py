from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    name = "createsu"

    def handle(self, *args, **options):
        User = get_user_model()

        if not User.objects.filter(email="stevic01@gmail.com").exists():
            User.objects.create_superuser(username="admin", email="stevic01@gmail.com", password="admin", first_name="vlado", last_name="stevic")