from django.apps import AppConfig
from django.db.models.signals import pre_save


class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_page'

    def ready(self):
        from .models import TheUsers
        from .signals import pre_save_signal_the_users
        TheUsers = self.get_model('TheUsers')
        pre_save.connect(pre_save_signal_the_users, sender=TheUsers)
