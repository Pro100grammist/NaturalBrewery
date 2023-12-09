from django.db import models
from django.core.validators import RegexValidator


def validate_number(value):
    validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Невірний формат номеру телефона.'
    )
    validator(value)


class CustomerRequestsDatabase(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=20, validators=[validate_number], default='+380')
    email = models.EmailField()
    comment = models.TextField(blank=True)
    time_of_receipt = models.DateTimeField(auto_now_add=True)
