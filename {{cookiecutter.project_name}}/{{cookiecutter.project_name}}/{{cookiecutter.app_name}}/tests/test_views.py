import pytest

from . import factories
from .. import views


pytestmark = pytest.mark.django_db


def test_index_view(rf):
    factories.AddressFactory(street='first street')
    factories.AddressFactory(title='second street')
    factories.AddressFactory(title='third street')

    response = views.index(rf)

    assert response.status_code == 200
    assert b'first street' in response.content
    assert b'second street' in response.content
    assert b'third street' in response.content


def test_adress_view(rf):
    address1 = factories.AddressFactory(
        number=100,
        street='test street',
    )
    response = views.letting(rf, 1)

    assert response.status_code == 200
    assert b'100' in response.content
    assert b'test street' in response.content
