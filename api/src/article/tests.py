from rest_framework import status
from rest_framework.test import APITestCase

from .models import Article, Sentence
from account.models import Account


APP_NAME = '/article/'


class ArticleTests(APITestCase):

    def test_new_article_1(self):
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
        self.assertEqual(Sentence.objects.count(), 1)
        self.assertEqual(Sentence.objects.first().sentence_text, 'some article content')

    def test_new_article_2(self):
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
            'full_text': 'One sentence.',
            'url': 'https://www.wikipedia.org/'
        }
        response_2 = self.client.post(APP_NAME + 'new', data_article, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Sentence.objects.count(), 1)
        self.assertEqual(Sentence.objects.first().sentence_text, 'One sentence')

    def test_new_article_3(self):
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
            'full_text': 'One sentence. Another sentence',
            'url': 'https://www.wikipedia.org/'
        }
        response_2 = self.client.post(APP_NAME + 'new', data_article, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Sentence.objects.count(), 2)
        self.assertEqual(Sentence.objects.first().sentence_text, 'One sentence')
        self.assertEqual(Sentence.objects.all()[1].sentence_text, 'Another sentence')

    def test_new_article_4(self):
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
            'full_text': 'One sentence! Another sentence',
            'url': 'https://www.wikipedia.org/'
        }
        response_2 = self.client.post(APP_NAME + 'new', data_article, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Sentence.objects.count(), 2)
        self.assertEqual(Sentence.objects.first().sentence_text, 'One sentence')
        self.assertEqual(Sentence.objects.all()[1].sentence_text, 'Another sentence')

    def test_new_article_5(self):
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
            'full_text': 'One sentence? Another sentence',
            'url': 'https://www.wikipedia.org/'
        }
        response_2 = self.client.post(APP_NAME + 'new', data_article, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Sentence.objects.count(), 2)
        self.assertEqual(Sentence.objects.first().sentence_text, 'One sentence')
        self.assertEqual(Sentence.objects.all()[1].sentence_text, 'Another sentence')

    def test_new_article_6(self):
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
            'full_text': 'One sentence... Another sentence',
            'url': 'https://www.wikipedia.org/'
        }
        response_2 = self.client.post(APP_NAME + 'new', data_article, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Sentence.objects.count(), 2)
        self.assertEqual(Sentence.objects.first().sentence_text, 'One sentence')
        self.assertEqual(Sentence.objects.all()[1].sentence_text, 'Another sentence')
