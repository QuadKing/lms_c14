import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestBookEndPoint:

    def test_that_anonymous_user_cannot_get_book(self):
        client = APIClient()
        response = client.get('/books/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_anonymous_user_cannot_create_book(self):
        client = APIClient()
        response = client.post('/books/',
                               {"title": "a", "genre": "c", "isbn": "916846781-8", "price": 428.32, "author": 94})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_admin_user_can_get_book(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/books/')
        assert response.status_code == status.HTTP_200_OK

    def test_that_admin_gets_400_due_to_invalid_data(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/books/',
                               {"title": "m", "genre": "c", "isbn": "6373", "price": 272, "author": 56})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
