from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('tasks/', include('tasks.urls')),
    ]

    def test_create_task_api(self):
        data = {
            'title': 'test',
            'description': 'another test'
        }
        url = reverse('create_tasks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


