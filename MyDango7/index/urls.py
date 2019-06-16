from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    #path('<int:id>.html', views.model_index),
]