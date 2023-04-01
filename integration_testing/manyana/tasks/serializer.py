from rest_framework.serializers import ModelSerializer
from tasks.models import Task


class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description')


class TaskReadSerializer(ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('id', 'title', 'description', 'completed', 'created_at')
        fields = read_only_fields


class TaskUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
