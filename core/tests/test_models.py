from django.test import TestCase

from model_mommy import mommy

from core.models import Task


class TaskTestCase(TestCase):

    def setUp(self):
        self.task = mommy.make(Task)

    def test_str(self):
        self.assertEquals(str(self.task), self.task.task)