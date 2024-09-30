# estoque/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    tipo_movimentacao = models.CharField(max_length=50, choices=[('Entrada', 'Entrada'), ('Saída', 'Saída')])

    def __str__(self):
        return f"{self.tipo_movimentacao} de {self.produto.nome} - {self.quantidade} unidades"
