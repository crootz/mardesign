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
    paginate_by = 5 #Increase the later


class ProductDetailView(DetailView):
    model = Product


def contact(request):
    return render(request, 'content/contact.html', {'title': 'Contact'})


