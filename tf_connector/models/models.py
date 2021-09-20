from django.db import models

from django.core.exceptions import ValidationError
from django.core import validators

# Create your models here.
class Status(models.Model):
    create_date = models.DateField()
    update_date = models.DateField()
    create_by_id = models.CharField(max_length=7)
    create_by_ip = models.CharField(max_length=15)
    update_by_ip = models.CharField(max_length=15)
    is_visible = models.BooleanField()
    is_active = models.BooleanField()
    is_verified = models.BooleanField()
    is_approved = models.BooleanField()
    is_archived = models.BooleanField()
    is_dormant = models.BooleanField()
    is_so_delete = models.BooleanField()
    def Meta(self):
        abstract = True


class TFconnector(Status):
    id = models.AutoField
    connector_name = models.CharField(max_length=20)
    connector_value = models.CharField(max_length=500)
    connector_desc = models.CharField(max_length=100)
    connector_remark = models.CharField(max_length=100)
    def Meta(self):
        return self.connector_name





