from rest_framework import serializers

from .models import Tabulation, Order
from menus.serializers import ProductSerializer


class OrderSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','uuid', 'quantity', 'state', 'tabulation', 'product')

class OrderSerializerRead(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id','uuid', 'quantity', 'state', 'tabulation', 'product')


class TabulationSerializer(serializers.ModelSerializer):
    orders = OrderSerializerRead(many=True, read_only=True)
    class Meta:
        model = Tabulation
        fields = ('id', 'uuid', 'establishment', 'origin', 'date', 'state','value','registered','orders')
