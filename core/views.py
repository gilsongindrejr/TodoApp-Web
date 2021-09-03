from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.utils import translation

from .models import Task


class IndexView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['lang'] = lang
        return context

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class CreateTaskView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['task', 'date']
    success_url = reverse_lazy('index')


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['task', 'date']
    success_url = reverse_lazy('index')


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
