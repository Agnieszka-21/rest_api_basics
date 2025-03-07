from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('product/<int:pk>/', views.product, name='product'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

