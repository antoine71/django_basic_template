import factory
from faker import Faker

from ..models import Address

fake = Faker()


class AddressFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Address

    number = fake.building_number()
    street = fake.street_name()
    city = fake.city()
    state = fake.country_code()
    zip_code = fake.postcode()
    country_iso_code = fake.country_code(representation='alpha-3')

