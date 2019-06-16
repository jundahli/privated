from django.urls import path
from . import views

urlpatterns = [
    # 首页的URL
    path('', views.index),
]