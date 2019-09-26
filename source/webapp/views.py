from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from .forms import *


class MainPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetails(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=pk)
        return context


class TaskCreate(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm
        return context

    def post(self, request):
        bound_form = TaskForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('main_url')


class TaskEdit(TemplateView):
    template_name = 'task_edit.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        context['form'] = form
        context['pk']=pk
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        bound_form = TaskForm(request.POST, instance=task)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('main_url')


class TaskDelete(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = pk
        return context

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('main_url')

