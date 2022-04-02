from django.urls import path

from shop.views import BaseView, ProductView, CategoryView, SearchProductsView, FilterView

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product-view'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category-view'),
    path('search/', SearchProductsView.as_view(), name='search'),
    path('filter/<slug:slug>/', FilterView.as_view(), name='filter'),



]