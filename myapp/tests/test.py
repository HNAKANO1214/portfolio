import pytest

from django.test import Client
from django.urls import reverse


def test_index_view_get(client: Client, db):
    '''Test index view get method'''
    # IndexViewのgetの結果が200化を確認する
    response = client.get(reverse('index'))
    assert response.status_code == 200


def test_detail_view_get(client: Client, db):
    '''Test detail view get method'''
    response = client.get(reverse('detail', kwargs={'pk': 1}))
    assert response.status_code == 200


def test_about_view_get(client: Client, db):
    '''Test about view get method'''
    response = client.get(reverse('about'))
    assert response.status_code == 200
