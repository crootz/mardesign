from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'content/index.html')


def products(request):
    return render(request, 'content/products.html', {'title': 'Products'})


def contact(request):
    return render(request, 'content/contact.html', {'title': 'Contact'})


