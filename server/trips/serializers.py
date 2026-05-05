from rest_framework.serializers import ModelSerializer

from accounts.serializers import UserSerializer
from trips.models import Trip


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = (
            'id',
            'created',
            'updated',
        )


class NestedTripSerializer(ModelSerializer):
    driver = UserSerializer()
    rider = UserSerializer()

    class Meta:
        model = Trip
        fields = '__all__'
        depth = 1
