from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Pizza, Order, Cart
from .forms import OrderCreationForm, OrderUpdateForm
from django.shortcuts import HttpResponseRedirect,render
from django.urls import reverse

class PizzaCreateView(CreateView):
    model = Pizza
    template_name = 'pizza/pizza_create.html'
    fields = ('name', 'preis', 'zutaten')

class PizzaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pizza
    template_name = 'pizza/pizza_delete.html'
    success_url = reverse_lazy('pizza_list')

    def test_func(self):
        return True

class PizzaDetailView(DetailView):
    model = Pizza
    template_name = 'pizza/pizza_detail.html'



class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizza/pizza_list.html'


class PizzaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pizza
    template_name = 'pizza/pizza_update.html'
    fields = ('name', 'preis', 'zutaten')

    def test_func(self):
        return True

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreationForm
    template_name = 'pizza/order_create.html'


class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = 'pizza/order_delete.html'
    success_url = reverse_lazy('order_list')

    def test_func(self):
        return True

class OrderDetailView(DetailView):
    model = Order
    template_name = 'pizza/order_detail.html'



class OrderListView(ListView):
    model = Order
    template_name = 'pizza/order_list.html'


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderUpdateForm
    template_name = 'pizza/order_update.html'

    def test_func(self):
        return True

class CartView(ListView):
    model = Cart
    template_name = 'pizza/cart.html'
    def update_cart(request,pk):
        cart = Cart.objects.all()[0]
        try:
            pizza = Pizza.objects.get(id=pk)
        except Pizza.DoesNotExist:
            pass
        except:
            pass
        if not pizza in cart.products.all():
            cart.products.add(pizza)
        else:
            cart.products.remove(pizza)
        total_price = 0.00
        for item in cart.products.all():
            total_price = total_price + float(item.preis)
        cart.total = total_price
        cart.save()
        return HttpResponseRedirect(reverse('cart_list'))