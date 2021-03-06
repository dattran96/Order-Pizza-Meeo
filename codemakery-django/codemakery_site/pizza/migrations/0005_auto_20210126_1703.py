# Generated by Django 3.1.4 on 2021-01-26 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20210125_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.CreateModel(
            name='OrderPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.order')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(through='pizza.OrderPizza', to='pizza.Pizza'),
        ),
    ]
