from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


def index(request):
    return render(request, 'content/index.html')


class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product List'
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product Detail'
        return context


def contact(request):
    return render(request, 'content/contact.html', {'title': 'Contact Us'})


def about(request):
    return render(request, 'content/about.html', {'title': 'About Us'})


