from django.http import HttpResponse


def index(request):
    return HttpResponse("Home Page")


def products(request):
    return HttpResponse("Product Page")


def contact(request):
    return HttpResponse("Contact Page")


