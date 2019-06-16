from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('download.html', views.download),
    path('login.html',views.login),
    path('index/<id>.html',views.ProductList.as_view(),{'name':'phone'}),
]