# financeiro/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contas/pagar/', views.contas_pagar_list, name='contas_pagar_list'),
    path('contas/pagar/adicionar/', views.conta_pagar_create, name='conta_pagar_create'),
    path('contas/pagar/<int:pk>/editar/', views.conta_pagar_update, name='conta_pagar_update'),
    path('contas/pagar/<int:pk>/deletar/', views.conta_pagar_delete, name='conta_pagar_delete'),
    
    path('contas/receber/', views.contas_receber_list, name='contas_receber_list'),
    path('contas/receber/adicionar/', views.conta_receber_create, name='conta_receber_create'),
    path('contas/receber/<int:pk>/editar/', views.conta_receber_update, name='conta_receber_update'),
    path('contas/receber/<int:pk>/deletar/', views.conta_receber_delete, name='conta_receber_delete'),
]
