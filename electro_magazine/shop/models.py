from django.db import models
from django.urls import reverse

from account.models import User


class Product(models.Model):

    STATUS_PRODUCT = [
        ('Have', 'Есть в наличие'),
        ('Havent', 'Временно отсутствует'),
    ]

    name = models.CharField(verbose_name='Наименование', max_length=255, unique=True)
    description = models.TextField(verbose_name='Описание товара', max_length=1024, null=True, blank=True)
    price_now = models.FloatField(verbose_name='Текущая цена товара')
    price_old = models.FloatField(verbose_name='Старая цена товара', null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Колличество товара на складе')
    photo = models.ImageField(verbose_name='Фото товара', upload_to='photo/%Y/%m/%d', null=True, blank=True)
    status = models.CharField(verbose_name='Стаус товара', max_length=15, choices=STATUS_PRODUCT, default='Have')
    discount = models.BooleanField(verbose_name='Cкидка на товар', null=False)
    created_ad = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_ad = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=255, unique=True, db_index=True)
    cat = models.ForeignKey('Category', verbose_name='Категория товара', on_delete=models.PROTECT,
                            null=True, blank=True)
    color = models.CharField(verbose_name='Цвет товара', max_length=255, null=True, blank=True)
    year = models.PositiveIntegerField(verbose_name='Год выпуска', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_detail', Product.objects.get(), kwargs={'slug': self.slug})


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Наименование категории', unique=True)
    subcategory = models.ForeignKey('Subcategory', verbose_name='Подкатегория категории', on_delete=models.PROTECT,
                                    null=True, blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Слаг категории', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category_detail', Category.objects.get(), kwargs={'slug': self.slug})


class Subcategory(models.Model):
    name = models.CharField(verbose_name='Под категория', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='слаг подкатегории', max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):

    owner = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE,
                                related_name='comments_products')
    body = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)
    active = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return str(self.id)

























