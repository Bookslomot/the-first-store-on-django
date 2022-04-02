from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from cart.mixins import CartMixins
from shop.forms import CommentForm
from shop.models import Product, Category, Comment


class BaseView(CartMixins, ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'shop/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cart'] = self.cart
        return context


class ProductView(CartMixins, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm
        return context

    """ Коментарии к продукту """

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST or None)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.product = self.get_object()
            self.object.owner = request.user
            self.object.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CategoryView(CartMixins, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category_detail.html'
    slug_field = 'slug'

    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        context['categories'] = Category.objects.all()
        context['self_categories'] = Category.objects.filter(slug=self.kwargs['slug']).first()
        context['colors'] = Product.objects.filter(cat__slug=self.kwargs['slug']).values('color').distinct()
        context['years'] = Product.objects.filter(cat__slug=self.kwargs['slug']).values('year').distinct()
        return context


class FilterView(CartMixins, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/category_detail.html'
    slug_field = 'slug'

    def get_queryset(self):
        return Product.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(color__in=self.request.GET.getlist('color'))).filter(cat__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        context['categories'] = Category.objects.all()
        context['self_categories'] = Category.objects.filter(slug=self.kwargs['slug']).first()
        context['colors'] = Product.objects.filter(cat__slug=self.kwargs['slug']).values('color').distinct()
        context['years'] = Product.objects.filter(cat__slug=self.kwargs['slug']).values('year').distinct()
        return context


class SearchProductsView(CartMixins, ListView):
    """ Поиск по названию товара на главной странице"""
    template_name = 'shop/main.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(name__iregex=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cart'] = self.cart
        context['q'] = self.request.GET.get('q')
        return context







































