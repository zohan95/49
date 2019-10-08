from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from webapp.models import Task
from webapp.forms import TaskForm
from .utils import DetailView, UpdateView, DeleteView


class TaskDetails(DetailView):
    template_name = 'task/details.html'
    model = Task
    context_key = 'task'


class TaskCreate(CreateView):
    model = Task
    fields = ['summary', 'description', 'task_status', 'task_type']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('main_url')


class TaskEdit(UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    form_class = TaskForm
    redirect_url = 'main_url'


class TaskDelete(DeleteView):
    template_name = 'task/task_delete.html'
    redirect_url = 'main_url'
    model = Task


class MainPage(ListView):
    template_name = 'task/index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3
    paginate_orphans = 1


