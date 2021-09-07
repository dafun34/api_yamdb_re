from django.contrib.auth.models import AbstractUser
from django.db import models


class Roles(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    bio = models.TextField(null=True, blank=None)
    email = models.EmailField(blank=False, unique=True,)
    role = models.CharField(max_length=50, choices=Roles.choices,
                            verbose_name='Роль')
    username = models.CharField(max_length=30, unique=True,
                                blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True,
                              blank=False, null=False)

    @property
    def is_admin(self):
        return self.is_staff or self.role == Roles.ADMIN

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR
