import random

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from mixer.backend.django import mixer

from .models import Author
from .views import AuthorModelViewSet


class AuthorTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='test', password='qwerty')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        force_authenticate(request, user=self.user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthorClientTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='test', password='qwerty')
        self.author = mixer.blend(Author, birthday_year=mixer.sequence(lambda c: int(random.random()*2000)))

    def test_get_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        self.client.login(username='test', password='qwerty')
        response = self.client.post('/api/authors/', {
            "first_name": "Федор",
            "last_name": "Достоевский",
            "birthday_year": 1820
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(pk=response.data.get('id'))
        self.assertEqual(author.last_name, 'Достоевский')
