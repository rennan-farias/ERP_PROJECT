# financeiro/models.py
from django.db import models
from vendas.models import Pedido

class ContaPagar(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao


class ContaReceber(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_recebimento = models.DateField()
    recebido = models.BooleanField(default=False)

    def __str__(self):
        return f"Recebimento de Pedido {self.pedido.id} - {self.valor} R$"
