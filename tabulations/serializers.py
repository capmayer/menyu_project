from rest_framework import serializers

from .models import Tabulation, Order
from menus.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ('uuid', 'quantity', 'product', 'state', 'tabulation')

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        #check http://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
        
        return order

class TabulationSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Tabulation
        fields = ('uuid', 'establishment', 'origin', 'date', 'state','value','orders')
