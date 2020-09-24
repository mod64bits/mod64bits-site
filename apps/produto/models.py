from decimal import Decimal
from django.db.models import signals
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from core.signals import create_slug


class Produto(models.Model):
    nome = models.CharField('Produto Nome', max_length=30)
    descricao = models.TextField('Descrição')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    valor = models.DecimalField('Valor Total', max_digits=13, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.00'))])
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('produtos:produto', args=(self.slug,))

    def __str__(self):
        return f'Produto: {self.nome}'


signals.post_save.connect(create_slug, sender=Produto)
