from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from .models import Hospital

hospital_mapping = {
    "facility_name": "Facility_n",
    "facility_type": "Facility_t",
    "ward": "Ward",
    "ownership": "Ownership",
    "lon": "Long",
    "lat": "Lat",
    "geom": "POINT",
}

hospital_shp = Path(__file__).resolve().parent / "data" / "Hospitals.shp"


def run(verbose=True):
    lm = LayerMapping(Hospital, str(hospital_shp), hospital_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
