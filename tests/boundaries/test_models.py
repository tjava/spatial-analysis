import pytest

def test_boundary_str(base_boundary):
    """Test the custom boundary model string representation"""
    assert base_boundary.__str__() == f"{base_boundary.name}"

