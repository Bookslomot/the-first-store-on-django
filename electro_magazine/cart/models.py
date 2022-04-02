from django.db import models
from django.utils import timezone

from account.models import User
from shop.models import Product


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)

    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)

    qty = models.PositiveIntegerField(verbose_name='Колличество товара', default=1)

    final_price = models.IntegerField(verbose_name='Итоговая цена')

    class Meta:
        verbose_name = 'Продукт корзины'
        verbose_name_plural = 'Продукты корзины'

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price_now
        super().save(*args, **kwargs)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE, null=True)

    products = models.ManyToManyField(CartProduct, verbose_name='Товар корзины', blank=True,
                                      related_name='related_cart')

    total_products = models.PositiveIntegerField(verbose_name='Общее колличество товаров', default=0)

    final_price = models.IntegerField(verbose_name='Финальная цена', default=0)

    in_order = models.BooleanField(verbose_name='Заказ', default=False)

    for_anonymous_user = models.BooleanField(verbose_name='Анонимный пользователь ', default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    phone = models.CharField(verbose_name='Телефон', max_length=20, null=True, blank=True)

    address = models.CharField(verbose_name='Адрес', max_length=255, null=True, blank=True)

    orders = models.ManyToManyField('Order', verbose_name='Заказы', related_name='related_customer')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупаетели'

    def __str__(self):
        return f'Покупатель {self.user.username}'


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполняется'),
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка'),
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE,
                                 related_name='related_orders')

    first_name = models.CharField(verbose_name='Имя', max_length=255)

    last_name = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True)

    phone = models.CharField(verbose_name='Телефон', max_length=20)

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)

    address = models.CharField(verbose_name='Адрес', max_length=255)

    status = models.CharField(verbose_name='Статус заказа', max_length=100,
                              choices=STATUS_CHOICES, default=STATUS_NEW)

    buying_type = models.CharField(verbose_name='Тип заказа', max_length=100,
                                   choices=BUYING_TYPE_CHOICES, default=BUYING_TYPE_DELIVERY)

    comment = models.TextField(verbose_name='Коментарий к заказу', max_length=1024, null=True, blank=True)

    created_at = models.DateTimeField(verbose_name='Время создания заказа', auto_now=True)

    order_date = models.DateTimeField(verbose_name='Желаемая дата получения заказа', default=timezone.now)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)


























