import factory
import factory.fuzzy
from factory import random
from faker import Factory as FakerFactory
from factory.fuzzy import BaseFuzzyAttribute
import random as rand
from django.contrib.gis.geos import Point, Polygon, MultiPolygon

faker = FakerFactory.create()

class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(rand.uniform(-180.0, 180.0),
            rand.uniform(-90.0, 90.0))


class FuzzyPolygon(factory.fuzzy.BaseFuzzyAttribute):
    """Yields random polygon"""
    def __init__(self, length=None, **kwargs):
        if length is None:
            length = random.randgen.randrange(3, 20, 1)
        if length < 3:
            raise Exception("Polygon needs to be 3 or greater in length.")
        self.length = length
        super().__init__(**kwargs)

    def get_random_coords(self):
        return (
            faker.longitude(),
            faker.latitude(),
        )

    def fuzz(self):
        prefix = suffix = self.get_random_coords()
        coords = [self.get_random_coords() for __ in range(self.length - 1)]
        return Polygon([prefix] + coords + [suffix])


class FuzzyMultiPolygon(factory.fuzzy.BaseFuzzyAttribute):
    """Yields random multipolygon"""
    def __init__(self, length=None, **kwargs):
        if length is None:
            length = random.randgen.randrange(2, 20, 1)
        if length < 2:
            raise Exception("MultiPolygon needs to be 2 or greater in length.")
        self.length = length
        super().__init__(**kwargs)

    def fuzz(self):
        polygons = [FuzzyPolygon().fuzz() for __ in range(self.length)]
        return MultiPolygon(*polygons)