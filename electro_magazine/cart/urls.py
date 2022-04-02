from django.urls import path

from cart.views import CartView, AddCartView, DeleteFromCartView, ChangeGTYCartView, CheckoutView, MakeOrderView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<slug:slug>', AddCartView.as_view(), name='add-to-cart'),
    path('delite-to-cart/<slug:slug>', DeleteFromCartView.as_view(), name='delete-to-cart'),
    path('change-gty-to-cart/<slug:slug>', ChangeGTYCartView.as_view(), name='change-gty-to-cart'),
    path('check-out/', CheckoutView.as_view(), name='check-out'),
    path('make-order/', MakeOrderView.as_view(), name='make-order'),

]
