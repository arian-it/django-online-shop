from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from product.models import Product
from .cart_module import Cart


class AddCartView(View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        size = request.POST.get("size")
        color = request.POST.get("color")

        try:
            quantity = int(request.POST.get("quantity", 1))
        except ValueError:
            quantity = 1

        if quantity < 1:
            quantity = 1

        if not size or not color:
            return redirect("product:product_detail", pk=pk)

        cart = Cart(request)
        cart.add(product=product, size=size, color=color, quantity=quantity,)
        return redirect("cart:cart_detail")


class CartDetailView(View):

    def get(self, request):

        cart = Cart(request)
        context = {
            "items": cart.get_items(),
            "total_price": cart.get_total_price(),
            "total_quantity": cart.get_total_quantity(),
        }

        return render(request, "cart/cart_detail.html", context)


class UpdateCartView(View):

    def post(self, request, key):

        try:
            quantity = int(request.POST.get("quantity"))
        except (TypeError, ValueError):
            quantity = 1

        cart = Cart(request)
        cart.update(key, quantity)

        return redirect("cart:cart_detail")


class RemoveCartView(View):

    def get(self, request, key):

        cart = Cart(request)
        cart.remove(key)

        return redirect("cart:cart_detail")


class ClearCartView(View):

    def get(self, request):

        cart = Cart(request)
        cart.clear()

        return redirect("cart:cart_detail")