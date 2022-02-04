from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from .filters import HospitalsFilter
from .models import Hospital
from .serializers import HospitalSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()[:20]
    serializer_class = HospitalSerializer
    # filter_class = HospitalsFilter
    filter_backends = (DjangoFilterBackend,)

    @action(detail=False, methods=["get"])
    def closest_hospitals(self, request):
        """Get Hospitals that are at least 3km or less from a users location"""
        longitude = request.GET.get("lon", None)
        latitude = request.GET.get("lat", None)

        if longitude and latitude:
            user_location = Point(float(longitude), float(latitude), srid=4326)
            closest_hospitals = Hospital.objects.filter(
                geom__distance_lte=(user_location, D(km=3))
            )[:20]
            serializer = self.get_serializer_class()
            serialized_hospitals = serializer(closest_hospitals, many=True)
            return Response(serialized_hospitals.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
