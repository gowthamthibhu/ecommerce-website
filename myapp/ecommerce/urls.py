from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/<int:item_id>", views.cart, name="cart")
]