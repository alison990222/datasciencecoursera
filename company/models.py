from django.db import models
from django.core.validators import int_list_validator

# Create your models here.

class clients(models.Model):
    username = models.CharField(max_length=100)
    location = models.CharField(max_length=50, null=True, default=None)
    timezone = models.DateTimeField(null=True, default=None)
    email = models.EmailField(max_length=50)