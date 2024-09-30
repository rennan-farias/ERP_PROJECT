# erp_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendas.urls')),  # Inclui as URLs do app 'vendas'
    path('estoque/', include('estoque.urls')),  # Inclui as URLs do app 'estoque'
    path('financeiro/', include('financeiro.urls')),  # Inclui as URLs do app 'financeiro'
]
