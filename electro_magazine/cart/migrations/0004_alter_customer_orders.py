# Generated by Django 4.0.2 on 2022-02-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_options_alter_cartproduct_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='cart.Order', verbose_name='Заказы'),
        ),
    ]
