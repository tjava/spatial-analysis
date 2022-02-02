from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Hospital(models.Model):
    facility_name = models.CharField(_("Hospital Name"), max_length=100)
    facility_type = models.CharField(_("Hospital Type"), max_length=100)
    ward = models.CharField(_("Ward"), max_length=100)
    ownership = models.CharField(_("Ownership"), max_length=100)
    lga = models.CharField(_("L.G.A"), max_length=100)
    lon = models.FloatField(_("Longitude"))
    lat = models.FloatField(_("Latitude"))

    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.facility_name
