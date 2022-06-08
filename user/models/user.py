

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # CHOICES
    USER_TYPE_ADMIN = 1
    USER_TYPE_CLIENT = 2
    USER_TYPE_ANONYMOUS = 3
    USER_TYPE_INVITED = 4

    USER_TYPE_CHOICES = (
        (USER_TYPE_ADMIN, 'admin'),
        (USER_TYPE_CLIENT, 'client'),
        (USER_TYPE_ANONYMOUS, 'anonymous'),
        (USER_TYPE_INVITED, 'invited')
    )

    phone = models.IntegerField(default=0, null=True)
    type_user = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=False)

    direction = models.CharField(max_length=100, null=True)

    bank_name = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=50, null=True)
    type_account = models.CharField(max_length=50, null=True)

    tigomoney_number = models.CharField(max_length=50, null=True)
    ci = models.CharField(max_length=50, null=True)





