from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm,
    UserChangeForm as DjangoUserChangeForm
)
from django import forms
from .models import Order, Pizza, OrderPizza


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizzas', 'customer']
        pizzas = forms.ModelMultipleChoiceField(
            queryset= Pizza.objects.all(),
            widget= forms.CheckboxSelectMultiple
        )

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizzas', 'customer']
        pizzas = forms.ModelMultipleChoiceField(
            queryset= Pizza.objects.all(),
            widget= forms.CheckboxSelectMultiple
        )

class OrderPizzaForm(forms.ModelForm):
    pizza = forms.ModelChoiceField(queryset=Pizza.objects.filter(id=1))
    class Meta:
        model = OrderPizza
        fields = '__all__'
