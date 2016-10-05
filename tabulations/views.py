from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from menus.models import Product
from menus.serializers import ProductSerializer
from .models import Tabulation, Order
from .serializers import TabulationSerializer, OrderSerializerWrite, OrderSerializerRead


class TabulationList(APIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)

    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        if request.user:
            establishment = self.request.user
            tabulations = Tabulation.objects.filter(establishment=establishment)
            serializer = TabulationSerializer(tabulations, many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = TabulationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TabulationDetail(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, uuid):
        try:
            return Tabulation.objects.get(uuid=uuid)
        except Tabulation.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        tabulation = self.get_object(uuid)
        serializer = TabulationSerializer(tabulation)
        return Response(serializer.data)

    def put(self, request, uuid, format=None):
        tabulation = self.get_object(uuid)
        serializer = TabulationSerializer(tabulation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        tabulation = self.get_object(uuid)
        tabulation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderDetail(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, uuid):
        try:
            return Order.objects.get(uuid=uuid)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        order = self.get_object(uuid)
        serializer = OrderSerializerWrite(order)
        return Response(serializer.data)

    def put(self, request, uuid, format=None):
        order = self.get_object(uuid)
        serializer = OrderSerializerWrite(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        order = self.get_object(uuid)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderList(APIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializerRead(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializerWrite(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
