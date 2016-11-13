from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework_extensions.cache.decorators import (
    cache_response
)

from .models import Menu, Product, Category
from .serializers import MenuSerializer, ProductSerializer, CategorySerializer


class MenuList(APIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)

    #should not exist
    def get(self, request, format=None):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetail(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, uuid):
        try:
            return Menu.objects.get(uuid=uuid)
        except Menu.DoesNotExist:
            raise Http404

    @cache_response()
    def get(self, request, uuid, format=None):
        menu = self.get_object(uuid)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, uuid, format=None):
        menu = self.get_object(uuid)
        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        menu = self.get_object(uuid)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDetail(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, uuid):
        try:
            return Product.objects.get(uuid=uuid)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        product = self.get_object(uuid)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, uuid, format=None):
        product = self.get_object(uuid)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        product = self.get_object(uuid)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
