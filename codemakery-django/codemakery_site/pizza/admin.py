from django.contrib import admin

from .models import Pizza,Order,OrderPizza,Cart, CartItem


admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(OrderPizza)
admin.site.register(Cart)
admin.site.register(CartItem)
