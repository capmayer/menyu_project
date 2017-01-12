from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Establishment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type_establishment = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    terms = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    terms = models.BooleanField(default=True)
