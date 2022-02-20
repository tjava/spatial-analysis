import factory
from faker import Factory as FakerFactory
from boundaries.models import Boundary
from hospitals.models import Hospital
from tests.fuzzy import FuzzyPoint, FuzzyMultiPolygon

faker = FakerFactory.create()

class HospitalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hospital

    facility_name = factory.LazyAttribute(lambda x: faker.name())
    facility_type = factory.LazyAttribute(lambda x: faker.name())
    ward = factory.LazyAttribute(lambda x: faker.name())
    ownership = factory.LazyAttribute(lambda x: faker.name())
    lga = factory.LazyAttribute(lambda x: faker.name())
    lon = factory.LazyAttribute(lambda x: faker.longitude())
    lat = factory.LazyAttribute(lambda x: faker.latitude())
    geom = FuzzyPoint()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create(*args, **kwargs)


class BoundaryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Boundary

    adm0_en = factory.LazyAttribute(lambda x: faker.name())
    adm0_pcode = factory.LazyAttribute(lambda x: faker.name())
    name = factory.LazyAttribute(lambda x: faker.name())
    pcode = factory.LazyAttribute(lambda x: faker.name()[:8])
    mpoly = FuzzyMultiPolygon(length=5)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create(*args, **kwargs)
