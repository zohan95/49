from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from .forms import *
from django.db.models import ProtectedError


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
        context['task'] = get_object_or_404(Task, pk=pk)
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
        context['pk'] = pk
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


class StatusView(TemplateView):
    template_name = 'status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = TaskStatus.objects.all()
        return context


class StatusEdit(TemplateView):
    template_name = 'status_edit.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        status = get_object_or_404(TaskStatus, pk=pk)
        context['form'] = StatusForm(instance=status)
        context['pk'] = status.pk
        return context

    def post(self, request, pk):
        status = get_object_or_404(TaskStatus, pk=pk)
        bound_form = StatusForm(request.POST, instance=status)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('status_url')


class StatusDelete(TemplateView):
    template_name = 'status_delete.html'

    def get_context_data(self, pk, **kwargs):
        status = get_object_or_404(TaskStatus, pk=pk)
        context = super().get_context_data(**kwargs)
        context['status'] = status
        return context

    def post(self, request, pk):
        status = get_object_or_404(TaskStatus, pk=pk)
        try:
            status.delete()
        except ProtectedError:
            return render(request, 'error_page.html')
        return redirect('status_url')


class TypeEdit(TemplateView):
    template_name = 'type_edit.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        task_type = get_object_or_404(TaskType, pk=pk)
        context['form'] = TypeForm(instance=task_type)
        context['pk'] = task_type.pk
        return context

    def post(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)
        bound_form = TypeForm(request.POST, instance=task_type)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('type_url')


class TypeDelete(TemplateView):
    template_name = 'type_delete.html'

    def get_context_data(self, pk, **kwargs):
        task_type = get_object_or_404(TaskType, pk=pk)
        context = super().get_context_data(**kwargs)
        context['type'] = task_type
        return context

    def post(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)
        task_type.delete()
        return redirect('type_url')


class TypeView(TemplateView):
    template_name = 'type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = TaskType.objects.all()
        return context


class TypeCreate(TemplateView):
    template_name = 'type_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TypeForm
        return context

    def post(self, request):
        bound_form = TypeForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('type_url')


class StatusCreate(TemplateView):
    template_name = 'status_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StatusForm
        return context

    def post(self, request):
        bound_form = StatusForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('status_url')
