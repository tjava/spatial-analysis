from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Hospital


class HospitalAdmin(LeafletGeoAdmin):
    list_display = ["facility_name", "facility_type", "ward", "ownership", "lga", "lon", "lat"]


admin.site.register(Hospital, HospitalAdmin)
