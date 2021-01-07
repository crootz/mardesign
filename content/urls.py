from django.urls import path
from . import views
from .views import ProductsListView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
