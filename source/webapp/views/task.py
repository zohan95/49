from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Task, STATUS_CHOICES
from django.forms.utils import ErrorList


class TaskDetails(DetailView):
    template_name = 'task/details.html'
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = ['summary', 'description', 'task_status', 'task_type', 'project']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('main_url')

    def form_valid(self, form):
        project = form.cleaned_data['project']
        if project.status == STATUS_CHOICES[0][0]:
            return super().form_valid(form)
        else:
            errors = form._errors.setdefault("project", ErrorList())
            errors.append(u"Вы выбрали неактивный проект!!!")
            return render(self.request, 'task/task_create.html', {'form': form})


class TaskEdit(UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    fields = ['summary', 'description', 'task_status', 'task_type', 'project']
    success_url = reverse_lazy('main_url')

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        if task.project.status == STATUS_CHOICES[0][0]:
            return super().get(self, request, *args, **kwargs)
        else:
            raise Http404


class TaskDelete(DeleteView):
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('main_url')
    model = Task

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        if task.project.status == STATUS_CHOICES[0][0]:
            return super().get(self, request, *args, **kwargs)
        else:
            raise Http404


class MainPage(ListView):
    template_name = 'task/index.html'
    model = Task
    paginate_by = 3
    paginate_orphans = 1
