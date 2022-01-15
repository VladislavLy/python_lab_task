from django.contrib import admin
from .models import TheUsers


@admin.register(TheUsers)
class TheUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
