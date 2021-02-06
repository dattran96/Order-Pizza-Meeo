from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(max_length=150)
    preis = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    zutaten = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pizza_detail', args=[str(self.id)])

CHOICES = (
    ("Order Recieved", "Order Recieved"),
    ("Baking", "Baking"),
    ("Baked", "Baked"),
    ("Out for delivery", "Out for delivery"),
    ("Order recieved", "Order recieved"),
)

class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza,through='OrderPizza',related_name='pizzas')
    #pizza = models.ForeignKey(Pizza,related_name="pizzas",on_delete =models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices = CHOICES )


    def __str__(self):
        return '%s' %(self.pk)

    def summe (self):
        summe = self.pizzas.all().aggregate(Sum('preis'))['preis__sum']
        return summe
    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

class OrderPizza(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE,related_name='order_pizzas',null= True,blank= True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='order_pizzas',null= True, blank= True)
    amount = models.IntegerField(default=0)

    def preis (self):
        #preis = self.pizza.preis
        preis = self.pizza.preis * self.amount
        return preis

class Cart(models.Model):
    products = models.ManyToManyField(Pizza, null = True, blank = True)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Card ID: %s" %(self.id)