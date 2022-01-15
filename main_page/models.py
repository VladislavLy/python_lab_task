from tabnanny import verbose
from django.db import models


class TheUsers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'All User'
