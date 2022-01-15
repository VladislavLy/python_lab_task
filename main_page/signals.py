from django.db.models.signals import pre_save

from .models import TheUsers


def pre_save_signal_the_users(sender, **kwargs):
    name = kwargs['instance'].name
    surname = kwargs['instance'].surname
    kwargs['instance'].name = str(name).capitalize()
    kwargs['instance'].surname = str(surname).capitalize()
pre_save.connect(pre_save_signal_the_users, sender=TheUsers)
