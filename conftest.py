import pytest
from pytest_factoryboy import register

from tests.factories import HospitalFactory, BoundaryFactory

register(HospitalFactory)
register(BoundaryFactory)


@pytest.fixture
def base_hospital(db, hospital_factory):
    new_hospital = hospital_factory.create()
    return new_hospital

@pytest.fixture
def base_boundary(db, boundary_factory):
    new_boundary = boundary_factory.create()
    return new_boundary

