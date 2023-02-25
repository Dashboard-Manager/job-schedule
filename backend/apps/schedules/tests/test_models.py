import pytest
from apps.schedules.tests.factory import TaskFactory
from apps.users.models import Profile


@pytest.mark.django_db
class TestTask:
    @pytest.fixture
    def task(self):
        return TaskFactory.create()

    def test_instance_task(self, task):
        assert isinstance(task.title, str)
        assert isinstance(task.description, str)
        assert isinstance(task.priority, str)
        assert isinstance(task.created_by, Profile)
        assert isinstance(task.assigned_user, Profile)
