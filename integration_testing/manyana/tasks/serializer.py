from rest_framework.serializers import ModelSerializer
from tasks.models import Task


class CreateTaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description')
