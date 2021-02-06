from django.db import models
from pizza.models import Pizza

# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Pizza, null = True, blank = True)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Card ID: %s" %(self.id)
