from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('create/', views.produto_create, name='produto_create'),
    path('update/<int:id>/', views.produto_update, name='produto_update'),
    path('delete/<int:id>/', views.produto_delete, name='produto_delete'),
]
