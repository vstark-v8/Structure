from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.conf import settings
from colorfield.fields import ColorField


class Client(TenantMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.schema_name


class Domain(DomainMixin):
    language = models.CharField(max_length=10,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)

class VisualConfig(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,related_name='VisualConfig')
    primary_color = ColorField(default='#000')
    second_color = ColorField(default='#222')
    third_color = ColorField(default='#555')
    letters_color = ColorField(default='#FFF')
    logo = models.ImageField(upload_to='/uploads/logo/')
    display_name = models.CharField(max_length=50)

class MailConfig(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='VisualConfig')
    host = models.CharField(max_length=50)
    port = models.IntegerField(max_length=3,default=587)
    mail = models.EmailField(max_length=50)
    pswd = models.CharField(max_length=50)
    tls = models.BooleanField(default=False)
    ssl = models.BooleanField(default=False)