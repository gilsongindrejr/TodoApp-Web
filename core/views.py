from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Task


class IndexView(ListView):
    model = Task
    template_name = 'index.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CreateTaskView(CreateView):
    model = Task
    template_name = 'create.html'
    fields = ['task', 'date']
    success_url = reverse_lazy('index')


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ['task', 'date']
    success_url = reverse_lazy('index')


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
