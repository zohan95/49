from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from webapp.models import Task
from webapp.forms import TaskForm
from .utils import DetailView


class TaskDetails(DetailView):
    template_name = 'task/details.html'
    model = Task
    context_key = 'task'


# class TaskCreate(TemplateView):
#     template_name = 'task/task_create.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = TaskForm
#         return context
#
#     def post(self, request):
#         bound_form = TaskForm(request.POST)
#         if bound_form.is_valid():
#             bound_form.save()
#             return redirect('main_url')


class TaskCreate(CreateView):
    model = Task
    fields = ['summary', 'description', 'task_status', 'task_type']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('main_url')


class TaskEdit(TemplateView):
    template_name = 'task/task_edit.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        context['form'] = form
        context['pk'] = pk
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        bound_form = TaskForm(request.POST, instance=task)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('main_url')


class TaskDelete(TemplateView):
    template_name = 'task/task_delete.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = pk
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('main_url')


class MainPage(ListView):
    template_name = 'task/index.html'
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3
    paginate_orphans = 1


