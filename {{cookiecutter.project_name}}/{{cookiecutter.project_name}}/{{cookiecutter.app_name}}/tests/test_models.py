import pytest

from . import factories


pytestmark = pytest.mark.django_db


def test_address():
    address = factories.AddressFactory(
        number=10,
        street='random street',
        zip_code= '12345',
        city='random city'
    )
    assert str(address) == '10 random street, 12345 random city'
