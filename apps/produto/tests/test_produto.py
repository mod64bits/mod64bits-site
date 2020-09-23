import pytest
from django.urls import reverse
from model_mommy import mommy
from apps.produto.models import Produto


@pytest.fixture
def produto(db):
    return mommy.make(Produto)


@pytest.fixture
def resp(client, produto):
    return client.get(reverse('produtos:produto', args=(produto.slug,)))


@pytest.fixture
def resp_prodto_nao_encontrado(client, produto):
    return client.get(reverse('produtos:produto', args=(produto.slug + 'produto_nao_existente',)))


def test_status_code_produto_nao_encontrado(resp_prodto_nao_encontrado):
    assert resp_prodto_nao_encontrado.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


