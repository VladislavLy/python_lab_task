from django.db.models.signals import pre_save
from .models import TheUsers
import re


def pre_save_signal_the_users(sender, **kwargs):
    name = re.sub("[^A-Za-z ]", "", kwargs['instance'].name).strip()
    surname = re.sub("[^A-Za-z ]", "", kwargs['instance'].surname).strip()
    kwargs['instance'].name = str(name).capitalize()
    kwargs['instance'].surname = str(surname).capitalize()
pre_save.connect(pre_save_signal_the_users, sender=TheUsers)
