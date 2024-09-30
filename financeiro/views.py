from django.shortcuts import render, redirect, get_object_or_404
from .models import ContaPagar, ContaReceber

# Contas a Pagar
def contas_pagar_list(request):
    contas = ContaPagar.objects.all()
    return render(request, 'contas_pagar_list.html', {'contas': contas})

def conta_pagar_create(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        data_vencimento = request.POST['data_vencimento']
        ContaPagar.objects.create(descricao=descricao, valor=valor, data_vencimento=data_vencimento)
        return redirect('contas_pagar_list')
    return render(request, 'contas_pagar_form.html')

def conta_pagar_update(request, pk):
    conta = get_object_or_404(ContaPagar, pk=pk)
    if request.method == 'POST':
        conta.descricao = request.POST['descricao']
        conta.valor = request.POST['valor']
        conta.data_vencimento = request.POST['data_vencimento']
        conta.save()
        return redirect('contas_pagar_list')
    return render(request, 'contas_pagar_form.html', {'conta': conta})

def conta_pagar_delete(request, pk):
    conta = get_object_or_404(ContaPagar, pk=pk)
    if request.method == 'POST':
        conta.delete()
        return redirect('contas_pagar_list')
    return render(request, 'contas_pagar_delete_confirm.html', {'conta': conta})

# Contas a Receber
def contas_receber_list(request):
    contas = ContaReceber.objects.all()
    return render(request, 'contas_receber_list.html', {'contas': contas})

def conta_receber_create(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        data_vencimento = request.POST['data_vencimento']
        ContaReceber.objects.create(descricao=descricao, valor=valor, data_vencimento=data_vencimento)
        return redirect('contas_receber_list')
    return render(request, 'contas_receber_form.html')

def conta_receber_update(request, pk):
    conta = get_object_or_404(ContaReceber, pk=pk)
    if request.method == 'POST':
        conta.descricao = request.POST['descricao']
        conta.valor = request.POST['valor']
        conta.data_vencimento = request.POST['data_vencimento']
        conta.save()
        return redirect('contas_receber_list')
    return render(request, 'contas_receber_form.html', {'conta': conta})

def conta_receber_delete(request, pk):
    conta = get_object_or_404(ContaReceber, pk=pk)
    if request.method == 'POST':
        conta.delete()
        return redirect('contas_receber_list')
    return render(request, 'contas_receber_delete_confirm.html', {'conta': conta})
