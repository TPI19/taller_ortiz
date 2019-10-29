from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass
    # add additional fields in here
    rol = models.IntegerField(default=2)
    telefono = models.CharField(max_length=15, null=True)
    direccion = models.CharField(max_length=250, null=True)