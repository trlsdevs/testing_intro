from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from tasks.serializer import CreateTaskSerializer


class CreateTask(CreateAPIView):
    serializer_class = CreateTaskSerializer
