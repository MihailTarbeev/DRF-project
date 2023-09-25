from django.contrib.auth.models import User
from django.db import models


class Programmers(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name
