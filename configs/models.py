from django.db import models
from django.contrib.auth.models import User

def qrcode_location(instance, filename):
    return 'geral/qrcodes/%s' % (filename)

class Qrcode(models.Model):
    qrcode = models.ImageField(upload_to=qrcode_location)

class Config(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    qrcode = models.ForeignKey(Qrcode)
