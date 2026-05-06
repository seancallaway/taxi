from base64 import b64decode
from json import loads

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

PASSWORD = 'pAssw0rd!'


def create_user(username='test@calnet.us', password=PASSWORD, group_name='rider'):
    group, _ = Group.objects.get_or_create(name=group_name)
    user = get_user_model().objects.create_user(
        username=username,
        first_name='Test',
        last_name='User',
        password=password,
    )
    user.groups.add(group)
    user.save()
    return user


class AuthenticationTest(APITestCase):

    def test_user_can_sign_up(self):
        response = self.client.post(reverse('sign_up'), data={
            'username': 'user@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': PASSWORD,
            'password2': PASSWORD,
            'group': 'rider',
        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['group'], user.group)

    def test_user_can_login(self):
        user = create_user()
        response = self.client.post(reverse('login'), data={
            'username': user.username,
            'password': PASSWORD,
        })

        # Parse payload data from access token.
        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = b64decode(f'{payload}==')
        payload_data = loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data['refresh'])
        self.assertEqual(int(payload_data['id']), user.id)
        self.assertEqual(payload_data['username'], user.username)
        self.assertEqual(payload_data['first_name'], user.first_name)
        self.assertEqual(payload_data['last_name'], user.last_name)
