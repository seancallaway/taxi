from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from trips.models import Trip
from trips.serializers import TripSerializer


class TripView(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
