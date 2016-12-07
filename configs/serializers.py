from rest_framework import serializers

from menus.serializers import MenuSerializer

from .models import Config

class ConfigSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    class Meta:
        model = Config
        fields = ('uuid', 'menu', 'is_premium')
