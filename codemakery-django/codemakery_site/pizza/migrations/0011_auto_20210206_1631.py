# Generated by Django 3.1.6 on 2021-02-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_auto_20210206_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pizza.cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='eachItem_Price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
