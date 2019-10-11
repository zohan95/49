from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskDetails(DetailView):
    template_name = 'task/details.html'
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = ['summary', 'description', 'task_status', 'task_type', 'project']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('main_url')


class TaskEdit(UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    fields = ['summary', 'description', 'task_status', 'task_type', 'project']
    success_url = reverse_lazy('main_url')


class TaskDelete(DeleteView):
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('main_url')
    model = Task


class MainPage(ListView):
    template_name = 'task/index.html'
    model = Task
    paginate_by = 3
    paginate_orphans = 1


