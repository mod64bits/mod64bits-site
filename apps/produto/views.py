from django.views.generic import ListView, DetailView
from apps.produto.models import Produto


class ProdutoList(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'produto/produto_list.html'

    def queryset(self):
        produtos = Produto.objects.order_by('criado_em').all()
        return produtos


class ProdutoDetalhe(DetailView):
    model = Produto
    template_name = 'produto/produto_detalhe.html'

    # def get_context_data(self, slug, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['produto'] = Produto.objects.get(slug=slug)
    #     return context


