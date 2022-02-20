import pytest


def test_hospital_str(base_hospital):
    """Test the custom hospital model string representation"""
    assert base_hospital.__str__() == f"{base_hospital.facility_name}"

