from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta, date

MEMBERSHIP_CHOICES = [
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
    ('Diamond', 'Diamond'),
]

MEMBERSHIP_DURATIONS = {
    'Silver': timedelta(days=30),
    'Gold': timedelta(days=90),
    'Diamond': timedelta(days=365),
}

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, blank=True, null=True)
    membership_start_date = models.DateField(blank=True, null=True)
    membership_expiry_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if self.membership_type and not self.membership_start_date:
            self.membership_start_date = date.today()
            self.membership_expiry_date = self.membership_start_date + MEMBERSHIP_DURATIONS.get(self.membership_type, timedelta(0))
        super().save(*args, **kwargs)
