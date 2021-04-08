from rest_framework import status
from rest_framework.test import APITestCase

from .models import Article
from account.models import Account


APP_NAME = '/article/'


class ArticleTests(APITestCase):

    def test_new_article(self):
        data_register = {
            'email': 'nonexisting@manavox.com',
            'password': 'passwordtest'
        }
        response_1 = self.client.post('/account/' + 'register', data_register, format='json')
        account = Account.objects.get(email='nonexisting@manavox.com')
        account.is_staff = True
        account.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response_1.data['token'])
        data_article = {
            'id_article': 1,
            'full_text': 'some article content',
            'url': 'https://www.wikipedia.org/'
        }
        response_2 = self.client.post(APP_NAME + 'new', data_article, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
