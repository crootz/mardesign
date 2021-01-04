from django.urls import path
from . import views
from .views import ProductsListView

app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('contact/', views.contact, name='contact'),
]