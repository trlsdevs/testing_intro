from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from tasks.serializer import TaskReadSerializer, TaskUpdateSerializer, TaskCreateSerializer
from tasks.models import Task


class HttpMethods:
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    PATCH = 'PATCH'


class TaskListCreateView(ListCreateAPIView):
    def get_queryset(self):
        return Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == HttpMethods.POST:
            return TaskCreateSerializer
        return TaskReadSerializer


class TaskRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    lookup_field = 'id'

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskUpdateSerializer
        return TaskReadSerializer
