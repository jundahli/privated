from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    # 首页的URL
    path('', cache_page(timeout=10,cache='MyDjango',key_prefix='MyDjangoURL')(views.index),name='index'),
    path('ShoppingCar.html',views.ShoppingCarView,name='ShoppingCar'),
    path('message.html',views.messageView,name='message'),
    path('pagination/<int:page>.html',views.paginationView,name="pagination"),
]