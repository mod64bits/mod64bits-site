from django.contrib.admin import ModelAdmin, register

from apps.produto.models import Produto


@register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = ('nome', 'descricao', 'slug', 'valor', 'criado_em')
    ordering = ('criado_em',)
