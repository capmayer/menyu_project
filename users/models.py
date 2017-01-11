from django.db import models

# Create your models here.
class Establishment(models.Model):
    user = models.OneToOne(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type_establishment = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    terms = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOne(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default="")
    phone = models.CharField(max_length=20, null=True)
    terms = models.BooleanField(default=True)
