from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    description = models.TextField(blank=True)

    def __str__(self):
        return "User(<{}>)".format(self.username)
