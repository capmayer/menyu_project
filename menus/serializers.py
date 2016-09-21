from rest_framework import serializers

from .models import Product, Category, Menu

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','owner', 'name', 'description', 'value', 'local_code', 'uuid')

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('owner', 'name', 'description', 'local_code', 'uuid', 'products')

class MenuSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('owner', 'name', 'id', 'uuid', 'categories')
