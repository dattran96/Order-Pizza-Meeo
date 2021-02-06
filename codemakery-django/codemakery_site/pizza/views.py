from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Pizza, Order, Cart, CartItem
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

#class CartView(ListView):
def cart_view(request):
    #if not request.session.session_key:
       # request.session.create()
    #session_id = request.session.session_key

    #try:
       # mycart_id = request.session[session_id]
   # except:
        #mycart_id = None

    #if mycart_id is not None:
    mycart = Cart.objects.get(id = 18)
    context = {"cart": mycart}
    #else:
        #context = {"empty": True, "message": "No items in your cart, please order pizza"}
    template = 'pizza/cart.html'

    return render(request,template,context)


def update_cart(request,pk):

    try:
        quantity = request.GET.get('quantity')
        update_quantity = True
    except:
        quantity = None
        update_quantity = False

    #try:
        #mycart_id = request.session['cart_id']
    #except:
        #new_cart = Cart()
        #new_cart.save()
        #request.session['card_id'] = new_cart.id
       # mycart_id = new_cart.id


    cart = Cart.objects.get(id = 18)
    #try:
    pizza = Pizza.objects.get(id=pk)
    #except Pizza.DoesNotExist:
       # pass
   # except:
     #   pass

    cart_item, created  = CartItem.objects.get_or_create(product=pizza, cart=cart)
    if created:
        print("Already have this kind of product")
    if  update_quantity and quantity:
        if int(quantity) == 0:
            cart_item.delete()
        else :
            cart_item.quantity = quantity
            cart_item.save()
    else:
        pass

    #if not cart_item in cart.items.all():
     #   cart.items.add(cart_item)
    #else:
     #   cart.items.remove(cart_item)


    total_price = 0.00

    for item in cart.cartitem_set.all():
        eachItem_price  = float(item.product.preis)*item.quantity
        total_price = total_price + float(eachItem_price)
    cart.total = total_price
    cart.save()
    return HttpResponseRedirect(reverse('cart_list'))