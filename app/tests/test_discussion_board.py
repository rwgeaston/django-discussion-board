from unittest import TestCase
from unittest.mock import ANY

from django.apps import apps
from django.test import Client
from rest_framework import status

from discussion_board import models


class DiscussionBoardGetTest(TestCase):
    def setUp(self):
        self.client = Client()
        User = apps.get_model(models.User)
        User.objects.all().delete()
        robert = User.objects.create(username='robert')
        guillaume = User.objects.create(username='guillaume')
        User.objects.create(username='joel')

        entity1 = models.Entity.objects.create(guid='1234')
        models.Entity.objects.create(guid='5678')

        thread1 = models.Thread.objects.create(
            title="Robert's Exciting Thread",
            owner=robert,
        )

        thread1.participants.set([robert, guillaume])

        thread2 = models.Thread.objects.create(
            title="Robert's Private Thread",
            owner=robert,
            entity=entity1,
        )

        thread2.participants.set([robert])

        models.Message.objects.create(
            text="What a great message",
            author=robert,
            thread=thread1,
        )
        self.maxDiff = None

    def tearDown(self):
        models.Message.objects.all().delete()
        models.Thread.objects.all().delete()
        models.Entity.objects.all().delete()
        User = apps.get_model(models.User)

        User.objects.all().delete()

    def test_user_gets(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'count': 3,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'username': 'robert',
                        'threads': [ANY, ANY],
                        'owned_threads': [ANY, ANY]
                    },
                    {
                        'username': 'guillaume',
                        'threads': [ANY],
                        'owned_threads': []
                    },
                    {
                        'username': 'joel',
                        'threads': [],
                        'owned_threads': []
                    }
                ]
            }
        )

        response = self.client.get('/api/users/robert/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'username': 'robert',
                'threads': [ANY, ANY],
                'owned_threads': [ANY, ANY]
            },
        )

        response = self.client.get('/api/users/guillaume/threads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [{
                    'id': ANY,
                    'entity': None,
                    'owner': 'robert',
                    'participants': ['robert', 'guillaume'],
                    'title': "Robert's Exciting Thread",
                    'creation': ANY,
                }],
            },
        )

        response = self.client.get('/api/users/robert/threads/')
        self.assertEqual(response.json()['count'], 2)

        response = self.client.get('/api/users/joel/threads/')
        self.assertEqual(response.json()['count'], 0)

        response = self.client.get('/api/users/robert/owned_threads/')
        self.assertEqual(response.json()['count'], 2)

        response = self.client.get('/api/users/guillaume/owned_threads/')
        self.assertEqual(response.json()['count'], 0)

        response = self.client.get('/api/users/robert/messages/')
        self.assertEqual(response.json()['count'], 1)

        response = self.client.get('/api/users/guillaume/messages/')
        self.assertEqual(response.json()['count'], 0)

    def test_thread_gets(self):
        response = self.client.get('/api/threads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'count': 2,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': ANY,
                        'entity': None,
                        'owner': 'robert',
                        'participants': ['robert', 'guillaume'],
                        'title': "Robert's Exciting Thread",
                        'creation': ANY,
                    },
                    {
                        'id': ANY,
                        'entity': '1234',
                        'owner': 'robert',
                        'participants': ['robert'],
                        'title': "Robert's Private Thread",
                        'creation': ANY,
                    },
                ],
            },
        )
