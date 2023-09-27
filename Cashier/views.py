from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Product , Transaction , TransactionItem
from .serializers import TransactionSerializer, TransactionItemSerializer , ProductSerializer
from django.contrib.auth import get_user_model





class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]


class create_transaction(generics.ListCreateAPIView):
    queryset = TransactionItem.objects.all()
    serializer_class = TransactionItemSerializer


class transactions_report(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer





