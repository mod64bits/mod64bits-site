from django.urls import path
from apps.produto.views import ProdutoList, ProdutoDetalhe

app_name = 'produtos'

urlpatterns = [
    path('<slug:slug>', ProdutoDetalhe.as_view(), name='produto'),
    path('', ProdutoList.as_view(), name='produtos'),
]
