from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='khaidoukova2015@yandex.ru',
            first_name='admin',
            last_name='skypro',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )

        user.set_password('320670')
        user.save()
