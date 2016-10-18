from django.contrib import admin
from .models import Qrcode, Config
# Register your models here.
admin.site.register(Qrcode)
admin.site.register(Config)
