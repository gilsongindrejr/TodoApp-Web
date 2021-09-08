from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.utils import translation

from .models import Task
from .forms import RegisterForm


class IndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['lang'] = lang
        context['user'] = self.request.user.first_name
        return context

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['task', 'date']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['task', 'date']
    success_url = reverse_lazy('index')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    success_message = 'User create successfully'
