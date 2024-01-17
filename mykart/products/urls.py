from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('product_list',views.list_products,name='list_product'),
    path('product_details/<pk>',views.detail_products,name='detail_products')
]
