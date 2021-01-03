from django.urls import path

from . import views

app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
]