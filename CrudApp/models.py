from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator

class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(100)]
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantidade_em_estoque = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome