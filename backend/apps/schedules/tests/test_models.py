import pytest
from apps.schedules.tests.factory import TaskFactory, JobFactory
from apps.schedules.services import get_hours
from apps.users.models import User
import datetime
from faker import Faker


faker = Faker()


@pytest.mark.django_db
class TestTask:
    @pytest.fixture
    def task(self, *args, **kwargs):
        return TaskFactory.create(*args, **kwargs)

    def test_instance_task(self, task):
        assert isinstance(task.title, str)
        assert isinstance(task.description, str)
        assert isinstance(task.priority, str)
        assert isinstance(task.created_by, User)
        assert isinstance(task.assigned_user, User)

    def custom_task(self, *args, **kwargs):
        return TaskFactory.create(*args, **kwargs)

    def test_title_length(self):
        tsk = self.custom_task(title=faker.text(max_nb_chars=255))
        assert len(tsk.title) <= 255

    def test_description_length(self):
        tsk = self.custom_task(description=faker.text(max_nb_chars=2000))
        assert len(tsk.description) <= 2000

    def test_priority_choices(self):
        tsk = self.custom_task(priority="lowest")
        assert tsk.priority == "lowest"

        tsk = self.custom_task(priority="high")
        assert tsk.priority == "high"

    def test_created_by(self):
        author = User.objects.create(username="author")
        tsk = self.custom_task(created_by=author)
        assert tsk.created_by == author

    def test_assigned_user(self):
        performer = User.objects.create(username="performer")
        tsk = self.custom_task(assigned_user=performer)
        assert tsk.assigned_user == performer

    def test_task_string_representation(self):
        tsk = self.custom_task(title="Test task")
        assert str(tsk) == "Test task"



@pytest.mark.django_db
class TestJob:
    @pytest.fixture
    def job(self, *args, **kwargs):
        return JobFactory.create(*args, **kwargs)

    def test_str_job(self, job):
        assert (
            str(job) == f"{job.user} worked by {job.hours} and {job.extra_hours} hours"
        )

    def test_hours(self, job):
        assert job.hours == min(
            divmod((job.start_job - job.end_job).total_seconds(), 3600)[0], 8
        )

    def test_extra_hours(self, job):
        assert job.extra_hours == max(
            0, divmod((job.start_job - job.end_job).total_seconds(), 3600)[0] - 8
        )

    def test_get_hours(self):
        start_job_str = "2022-02-22T10:00:00"
        end_job_str = "2022-02-22T12:30:00"
        expected_hours = 2
        # start_job = datetime.datetime.strptime(start_job_str, "%Y-%m-%dT%H:%M:%S")
        # end_job = datetime.datetime.strptime(end_job_str, "%Y-%m-%dT%H:%M:%S")

        start_job = datetime.datetime.fromisoformat(start_job_str)
        end_job = datetime.datetime.fromisoformat(end_job_str)

        assert get_hours(start_job=start_job_str, end_job=end_job_str) == expected_hours
        assert get_hours(start_job, end_job) == expected_hours
