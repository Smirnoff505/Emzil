from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    code = models.CharField(max_length=10, verbose_name='Код для верификации')
    is_active = models.BooleanField(default=False, verbose_name='Верификация')
    data_create_user = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(randint(100000, 999999))
        super().save(*args, **kwargs)
