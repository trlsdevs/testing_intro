import pytest

from tasks.models import Task


@pytest.mark.django_db
def test_taks_created():
    Task.objects.create(
        title="test",
        description='test'
    )
    assert Task.objects.count() == 1
