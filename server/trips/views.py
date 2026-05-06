from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from trips.models import Trip
from trips.serializers import NestedTripSerializer


class TripView(ReadOnlyModelViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    permission_classes = [IsAuthenticated,]
    serializer_class = NestedTripSerializer

    def get_queryset(self):
        user = self.request.user
        if user.group == 'driver':
            return Trip.objects.filter(
                Q(status=Trip.REQUESTED) | Q(driver=user)
            )
        if user.group == 'rider':
            return Trip.objects.filter(rider=user)

        return Trip.objects.none()
