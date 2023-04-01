from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Task


class TaskTests(APITestCase):
    def setUp(self):
        self.task1 = Task.objects.create(title='Task 1')
        self.task2 = Task.objects.create(title='Task 2', completed=True)

    def test_get_task_list(self):
        url = reverse('task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_task_detail(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {'title': 'New Task', 'description': 'NEw description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.get(id=3).title, 'New Task')

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {'title': 'Updated Task', 'completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task1.id).title, 'Updated Task')
        self.assertTrue(Task.objects.get(id=self.task1.id).completed)

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
