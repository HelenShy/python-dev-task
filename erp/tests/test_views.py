import unittest
from django.test import TestCase
from rest_framework.test import APIClient

from accounts.models import UserProfileManager, UserProfile


def create_user():
    name = 'test'
    password = '1j3m4mm3'
    UserProfile.objects.create_user(name, password)


def login():
    name = 'test'
    password = '1j3m4mm3'
    data = {'username':name,
            'password':password}
    client = APIClient()
    resp = client.post('/api/v2/login/', data, format='json')
    return resp


def delete_user():
    name = 'test'
    UserProfile.objects.delete_user(name)


class TestApplicationView(unittest.TestCase):
    def setUp(self):
        create_user()

    def tearDown(self):
        delete_user()

    def test_agreements_view_set_401(self):
        client = APIClient()
        resp = client.get('/api/v2/agreements/', format='json')
        self.assertEqual(resp.status_code, 401)

    def test_agreements_view_set_200(self):
        auth = login()
        token = auth.json()['token']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.get('/api/v2/agreements/',  format='json')
        self.assertEqual(resp.status_code, 200)

    def test_payments_view_set_401(self):
        client = APIClient()
        resp = client.get('/api/v2/agreements/2/payments/', format='json')
        self.assertEqual(resp.status_code, 401)

    def test_payments_view_set_200(self):
        auth = login()
        token = auth.json()['token']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        resp = client.get('/api/v2/agreements/2/payments/',  format='json')
        self.assertEqual(resp.status_code, 200)


class TestAccountView(TestCase):
    def setUp(self):
        create_user()

    def tearDown(self):
        delete_user()

    def test_user_login(self):
        resp = login()
        assert resp.status_code == 200
