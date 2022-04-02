from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from account.forms import RegistrationForm, UpdateProfileUserForm
from account.models import User
from cart.models import Customer, Order
from shop.models import Category
from cart.mixins import CartMixins


class LoginUser(CartMixins, LoginView):
    model = User
    fields = ['username', 'password']
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        context['categories'] = Category.objects.all()
        return context


class RegistrationView(CartMixins, CreateView):
    form_class = RegistrationForm
    template_name = 'account/registration.html'

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.phone = form.cleaned_data['phone']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user, phone=form.cleaned_data['phone']
            )
            user = authenticate(
                username=new_user.username, password=form.cleaned_data['password']
            )
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form,
        }
        return render(request, 'account/registration.html', context)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        context['categories'] = Category.objects.all()
        return context


class ProfileView(CartMixins, View):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        orders = Order.objects.filter(customer=customer).order_by('-created_at')
        categories = Category.objects.all()
        form = UpdateProfileUserForm(request.POST or None)
        context = {
            'orders': orders,
            'customer': customer,
            'cart': self.cart,
            'categories': categories,
            'form': form
        }
        return render(request, 'account/profile.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UpdateProfileUserForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        orders = Order.objects.filter(customer=customer).order_by('-created_at')
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.username = form.cleaned_data['username']
            user.phone = form.cleaned_data['phone']
            user.save()
            Customer.objects.user = request.user.username
            return HttpResponseRedirect('/')
        context = {
            'orders': orders,
            'customer': customer,
            'form': form,
            'cart': self.cart,
            'categories': Category.objects.all(),
        }
        return render(request, 'account/profile.html', context)






















