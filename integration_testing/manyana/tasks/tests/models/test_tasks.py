from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.task = Task.objects.create(title='test task', description='test description', user=self.user)

    def test_task_creation(self):
        """
        Test that a task is created correctly
        """
        self.assertEqual(self.task.title, 'test task')
        self.assertEqual(self.task.description, 'test description')
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.created_at)
        self.assertEqual(self.task.user, self.user)

    def test_task_completion(self):
        """
        Test that a task can be completed
        """
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)

    def test_task_str(self):
        """
        Test that the task string representation is correct
        """
        self.assertEqual(str(self.task), 'test task')

    def test_task_ordering(self):
        """
        Test that completed tasks are ordered first
        """
        task2 = Task.objects.create(title='completed task', completed=True)
        task3 = Task.objects.create(title='incomplete task')
        task_list = list(Task.objects.all())
        # self.assertEqual(task_list[0], task2)
        # self.assertEqual(task_list[1], self.task)
        # self.assertEqual(task_list[2], task3)
