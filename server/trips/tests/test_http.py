from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.test_http import PASSWORD, create_user
from trips.models import Trip


class HttpTripTest(APITestCase):

    def setUp(self):
        self.user = create_user()
        self.client.login(username=self.user.username, password=PASSWORD)

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_address='A', drop_off_address='B', rider=self.user),
            Trip.objects.create(pick_up_address='B', drop_off_address='C', rider=self.user),
            Trip.objects.create(pick_up_address='C', drop_off_address='D'),
        ]
        response = self.client.get(reverse('trips:list'))

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected_trip_ids = [str(trip.id) for trip in trips[0:2]]
        actual_trip_ids = [trip.get('id') for trip in response.data]
        self.assertCountEqual(expected_trip_ids, actual_trip_ids)

    def test_user_can_retrieve_trip_by_id(self):
        trip = Trip.objects.create(pick_up_address='A', drop_off_address='B', rider=self.user)
        response = self.client.get(trip.get_absolute_url())

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(str(trip.id), response.data['id'])
