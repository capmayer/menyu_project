from rest_framework import serializers

from .models import Tabulation, Order
from menus.serializers import ProductSerializer
from seats.serializers import SeatSerializer


class OrderSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','uuid', 'quantity', 'state', 'tabulation', 'product')

class OrderSerializerRead(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id','uuid', 'quantity', 'state', 'tabulation', 'product', 'last_modified')


class TabulationSerializerRead(serializers.ModelSerializer):
    orders = OrderSerializerRead(many=True, read_only=True)
    origin = SeatSerializer(read_only=True)
    class Meta:
        model = Tabulation
        fields = ('id', 'uuid', 'establishment', 'origin', 'date', 'state','value','registered','orders', 'last_modified')

class TabulationSerializerWrite(serializers.ModelSerializer):
    orders = OrderSerializerRead(many=True, read_only=True)
    class Meta:
        model = Tabulation
        fields = ('id', 'uuid', 'establishment', 'origin', 'date', 'state','value','registered','orders')
