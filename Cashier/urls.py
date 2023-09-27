from django.contrib import admin
from django.urls import path
from .views import ProductListCreateView, ProductDetailView, transactions_report , create_transaction

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('transactions/create/', create_transaction.as_view(), name='create_transaction'),
    path('transactions/report/', transactions_report.as_view(), name='transactions_report'),
   
]