# vendas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Pedido, Produto, Venda, ItemVenda


# Página inicial
def home(request):
    return render(request, 'home.html')

# Listar clientes
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes_list.html', {'clientes': clientes})

# Adicionar cliente
def clientes_add(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        Cliente.objects.create(nome=nome, email=email, telefone=telefone, endereco=endereco)
        return redirect('clientes_list')
    return render(request, 'clientes_form.html')

# Editar cliente
def clientes_edit(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.endereco = request.POST.get('endereco')
        cliente.save()
        return redirect('clientes_list')
    return render(request, 'clientes_form.html', {'cliente': cliente})

# Deletar cliente
def clientes_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_list')
    return render(request, 'clientes_delete_confirm.html', {'cliente': cliente})

# Listar pedidos
def pedidos_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos_list.html', {'pedidos': pedidos})

# Adicionar pedido
def pedidos_add(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cliente = Cliente.objects.get(id=cliente_id)
        produto_id = request.POST.get('produto')
        produto = Produto.objects.get(id=produto_id)
        quantidade = int(request.POST.get('quantidade'))
        Pedido.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)
        return redirect('pedidos_list')
    return render(request, 'pedidos_form.html', {'produtos': produtos})

# Editar pedido
def pedidos_edit(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    produtos = Produto.objects.all()
    if request.method == 'POST':
        pedido.cliente_id = request.POST.get('cliente')
        pedido.produto_id = request.POST.get('produto')
        pedido.quantidade = int(request.POST.get('quantidade'))
        pedido.save()
        return redirect('pedidos_list')
    return render(request, 'pedidos_form.html', {'pedido': pedido, 'produtos': produtos})

# Deletar pedido
def pedidos_delete(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos_list')
    return render(request, 'pedidos_delete_confirm.html', {'pedido': pedido})

# Listar produtos
def produtos_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos_list.html', {'produtos': produtos})

# Adicionar produto
def produtos_add(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = float(request.POST.get('preco'))
        estoque = int(request.POST.get('estoque'))
        Produto.objects.create(nome=nome, preco=preco, estoque=estoque)
        return redirect('produtos_list')
    return render(request, 'produtos_form.html')

# Editar produto
def produtos_edit(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.preco = float(request.POST.get('preco'))
        produto.estoque = int(request.POST.get('estoque'))
        produto.save()
        return redirect('produtos_list')
    return render(request, 'produtos_form.html', {'produto': produto})

# Deletar produto
def produtos_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_list')
    return render(request, 'produtos_delete_confirm.html', {'produto': produto})

# vendas/views.py
def estoque_list(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque_list.html', {'produtos': produtos})


def venda_create(request):
    if request.method == 'POST':
        venda = Venda.objects.create()  # Cria uma nova venda
        produtos_ids = request.POST.getlist('produtos')
        quantidades = request.POST.getlist('quantidades')
        
        for produto_id, quantidade in zip(produtos_ids, quantidades):
            produto = Produto.objects.get(id=produto_id)
            ItemVenda.objects.create(venda=venda, produto=produto, quantidade=quantidade)
            produto.estoque -= int(quantidade)  # Atualiza o estoque
            produto.save()
        
        return redirect('venda_list')  # Redireciona para a lista de vendas
    
    produtos = Produto.objects.all()
    return render(request, 'venda_form.html', {'produtos': produtos})

def venda_list(request):
    vendas = Venda.objects.prefetch_related('itemvenda_set__produto').all()
    return render(request, 'venda_list.html', {'vendas': vendas})
