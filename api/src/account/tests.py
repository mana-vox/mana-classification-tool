from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Account


APP_NAME = '/account/'


class AccountTests(APITestCase):

    def test_register(self):
        data = {
            'email': 'nonexisting@manavox.com',
            'password': 'passwordtest'
        }
        response = self.client.post(APP_NAME + 'register', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)

    def test_login(self):
        data_register = {
            'email': 'nonexisting@manavox.com',
            'password': 'passwordtest'
        }
        _ = self.client.post(APP_NAME + 'register', data_register, format='json')
        data_login = {
            'username': 'nonexisting@manavox.com',
            'password': 'passwordtest'
        }
        response = self.client.post(APP_NAME + 'login', data_login, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data.keys())

    def test_logout(self):
        data_register = {
            'email': 'nonexisting@manavox.com',
            'password': 'passwordtest'
        }
        _ = self.client.post(APP_NAME + 'register', data_register, format='json')
        data_login = {
            'username': 'nonexisting@manavox.com',
            'password': 'passwordtest'
        }
        response_1 = self.client.post(APP_NAME + 'login', data_login, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response_1.data['token'])
        response_2 = self.client.post(APP_NAME + 'logout', {}, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.data['logout'], 'Logged out successfully')
        self.assertEqual(Token.objects.filter(user=Account.objects.get(email='nonexisting@manavox.com')).count(), 0)
