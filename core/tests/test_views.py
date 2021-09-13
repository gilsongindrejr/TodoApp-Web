from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy
from django.utils import timezone

from model_mommy import mommy

from users.models import CustomUserModel
from core.models import Task

from core.views import IndexView, CreateTaskView


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = mommy.make(CustomUserModel)
        self.task = Task(
            author=self.user,
            task='task to do',
            date=timezone.now(),
            created=timezone.now(),
            modified=timezone.now(),
        )
        self.task.save()

    def test_get_queryset(self):
        request = self.factory.get(reverse_lazy('index'))
        request.user = self.user
        response = IndexView.as_view()(request)
        qs = response.context_data['object_list'][0]
        self.assertEquals(qs.task, self.task.task)


class CreateTaskViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = mommy.make(CustomUserModel)
        self.data = {
            'author': self.user,
            'task': 'task to do',
            'date': '12/09/2021 21:30',
        }

    def test_form_valid(self):
        request = self.factory.post(reverse_lazy('create'), data=self.data)
        request.user = self.user
        response = CreateTaskView.as_view()(request)
        self.assertEquals(request._post['author'], self.user.email)
