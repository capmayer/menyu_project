import uuid
from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    def __str__(self):
        return str(self.owner) +" "+ self.name

class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories')
    local_code = models.CharField(max_length=20, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255, blank=True)
    value = models.FloatField()
    local_code = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.name
