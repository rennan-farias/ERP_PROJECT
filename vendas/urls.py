# vendas/urls.py
from django.urls import path
from . import views
from .views import venda_create, venda_list

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/add/', views.clientes_add, name='clientes_add'),
    path('clientes/edit/<int:id>/', views.clientes_edit, name='clientes_edit'),
    path('clientes/delete/<int:id>/', views.clientes_delete, name='clientes_delete'),

    # urls para pedidos
    path('pedidos/', views.pedidos_list, name='pedidos_list'),
    path('pedidos/add/', views.pedidos_add, name='pedidos_add'),
    path('pedidos/edit/<int:id>/', views.pedidos_edit, name='pedidos_edit'),
    path('pedidos/delete/<int:id>/', views.pedidos_delete, name='pedidos_delete'),

    # urls para produtos
    path('produtos/', views.produtos_list, name='produtos_list'),
    path('produtos/add/', views.produtos_add, name='produtos_add'),
    path('produtos/edit/<int:id>/', views.produtos_edit, name='produtos_edit'),
    path('produtos/delete/<int:id>/', views.produtos_delete, name='produtos_delete'),

    # urls para estoque
    path('estoque/', views.estoque_list, name='estoque_list'),

    path('vendas/', venda_list, name='venda_list'),
    path('vendas/adicionar/', venda_create, name='venda_create'),
]

