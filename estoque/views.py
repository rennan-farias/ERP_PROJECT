from django.shortcuts import render
from .models import Produto

# Create your views here.
def estoque_list(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque_list.html', {'produtos': produtos})
