import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.base.django_assertions import assert_contains
from apps.produto.models import Produto


@pytest.fixture
def produtos(db):
    return mommy.make(Produto, 3)


@pytest.fixture
def resp(client, produtos):
    return client.get(reverse('produtos:produtos'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_slug_produto(resp, produtos):
    for produto in produtos:
        assert_contains(resp, produto.slug)


