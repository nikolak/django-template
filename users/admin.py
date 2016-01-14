from django.contrib import admin

from .models import Person

@admin.register(Person)
class PersonAdminModel(admin.ModelAdmin):
    fields = ['username', 'last_login']
