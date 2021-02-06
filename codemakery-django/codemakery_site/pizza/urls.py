from django.urls import path

from .views import PizzaCreateView, PizzaDeleteView, PizzaDetailView, PizzaListView, PizzaUpdateView
from .views import OrderCreateView, OrderDeleteView, OrderDetailView, OrderListView, OrderUpdateView
from .views import cart_view, update_cart


urlpatterns = [
    path('pizza/<int:pk>/', PizzaDetailView.as_view(), name='pizza_detail'),
    path('pizza/<int:pk>/edit/', PizzaUpdateView.as_view(), name='pizza_update'),
    path('pizza/<int:pk>/delete/', PizzaDeleteView.as_view(), name='pizza_delete'),
    path('pizza/new/', PizzaCreateView.as_view(), name='pizza_create'),
    path('', PizzaListView.as_view(), name='pizza_list'),
    path('pizza/order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('pizza/order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('pizza/order/new/', OrderCreateView.as_view(), name='order_create'),
    path('order/', OrderListView.as_view(), name='order_list'),
    path('cart/', cart_view, name='cart_list'),
    path('cart/<int:pk>/', update_cart, name='cart_update'),
]




