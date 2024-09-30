from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.estoque_list, name='estoque_list'),
]
