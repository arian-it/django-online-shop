from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product, Color


class ProductDetailView(DetailView):
    model = Product

