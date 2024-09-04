from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Creates 5 fake user accounts'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            email = fake.email()
            mobile = fake.numerify('+##########')  # Generate a 10-digit phone number
            pin = fake.numerify('####')  # Generate a 4-digit PIN

            try:
                user = User.objects.create_user(
                    email=email,
                    mobile=mobile,m1
                    pin=pin
                )
                self.stdout.write(self.style.SUCCESS(f'Created user: {email} | Mobile: {mobile} | PIN: {pin}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to create user: {email}. Error: {str(e)}'))
