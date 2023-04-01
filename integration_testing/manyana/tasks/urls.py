from django.urls import path
from tasks.views import CreateTask

urlpatterns = [
    path('', CreateTask.as_view(), name='create_tasks'),
]
