from django.urls import path
from tasks.views import TaskListCreateView, TaskRetrieveUpdateView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:id>', TaskRetrieveUpdateView.as_view(), name='task-detail'),
]
