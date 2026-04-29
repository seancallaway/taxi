from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.test_http import PASSWORD, create_user
from trips.models import Trip


class HttpTripTest(APITestCase):

    def setUp(self):
        user = create_user()
        response = self.client.post(reverse('login'), data={
            'username': user.username,
            'password': PASSWORD,
        })
        self.access = response.data['access']

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_address='A', drop_off_address='B'),
            Trip.objects.create(pick_up_address='B', drop_off_address='C'),
        ]
        response = self.client.get(
            reverse('trips:list'),
            HTTP_AUTHORIZATION=f'Bearer {self.access}',
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected_trip_ids = [str(trip.id) for trip in trips]
        actual_trip_ids = [trip.get('id') for trip in response.data]
        self.assertCountEqual(expected_trip_ids, actual_trip_ids)
