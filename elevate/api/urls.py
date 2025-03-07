from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('product/<int:pk>/', views.product, name='product'),
]

