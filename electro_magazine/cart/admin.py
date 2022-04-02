from django.contrib import admin

from cart.models import CartProduct, Cart, Customer, Order


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):

    list_display = ('user', 'cart', 'qty', 'final_price',)
    list_display_links = ('user',)
    search_fields = ('user', 'cart')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('owner', 'total_products', 'final_price', 'for_anonymous_user', 'in_order')
    list_display_links = ('owner',)
    search_fields = ('owner',)
    list_filter = ('in_order', 'for_anonymous_user',)
    ordering = ('owner',)
    list_editable = ('in_order', 'for_anonymous_user',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone', 'address', )
    list_display_links = ('user',)
    search_fields = ('user',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'first_name', 'last_name', 'phone', 'cart', 'address', 'status', 'buying_type',
                    'created_at', 'order_date')
    list_display_links = ('customer',)
    search_fields = ('customer',)
    list_filter = ('status', 'buying_type', )


