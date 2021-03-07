from django.contrib import admin
from .models import *


class DomainInline(admin.TabularInline):
    model = Domain


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [DomainInline]
    list_display = ('schema_name', 'name')

admin.register(VisualConfig)
admin.register(MailConfig)
