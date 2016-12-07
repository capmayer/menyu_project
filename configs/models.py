import uuid
from django.db import models
from django.contrib.auth.models import User
from menus.models import Menu

def qrcode_location(instance, filename):
    return 'geral/qrcodes/%s' % (filename)

class Qrcode(models.Model):
    qrcode = models.ImageField(upload_to=qrcode_location)

class Config(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    qrcode = models.ForeignKey(Qrcode, blank=True)
    menu = models.ForeignKey(Menu, blank=True, null=True)
    STATES = (
        ('p', 'premium'),
        ('f', 'free'),
    )
    is_premium = models.CharField(max_length=1, choices=STATES, default='p')
