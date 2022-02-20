from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Hospital


class HospitalAdmin(LeafletGeoAdmin):
    list_display = ["pk", "facility_name", "facility_type", "ward", "ownership", "lga", "lon", "lat"]

    list_display_links = ["facility_name"]

admin.site.register(Hospital, HospitalAdmin)
