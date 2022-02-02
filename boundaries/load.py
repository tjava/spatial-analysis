from pathlib import Path

from django.contrib.gis.utils import LayerMapping

from .models import Boundary

boundary_mapping = {
    "adm0_en": "admin0Name",
    "adm0_pcode": "admin0Pcod",
    "name": "admin1Name",
    "pcode": "admin1Pcod",
    "mpoly": "MULTIPOLYGON",
}


boundary_shp = Path(__file__).resolve().parent / "data" / "Boundary.shp"


def run(verbose=True):
    lm = LayerMapping(Boundary, str(boundary_shp), boundary_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
