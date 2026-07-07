from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.AddCartView.as_view(), name='cart_add'),
    path("update/<str:key>/", views.UpdateCartView.as_view(), name="cart_update"),
    path("remove/<str:key>/", views.RemoveCartView.as_view(), name="cart_remove"),
    path("clear/", views.ClearCartView.as_view(), name="cart_clear"),

]

