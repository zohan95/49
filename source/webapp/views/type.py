from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView
from webapp.forms import TypeForm
from webapp.models import TaskType
from .utils import ListView


class TypeEdit(TemplateView):
    template_name = 'type/type_edit.html'

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
    template_name = 'type/type_delete.html'

    def get_context_data(self, pk, **kwargs):
        task_type = get_object_or_404(TaskType, pk=pk)
        context = super().get_context_data(**kwargs)
        context['type'] = task_type
        return context

    def post(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)
        try:
            task_type.delete()
        except ProtectedError:
            return render(request, 'error_page.html')
        return redirect('type_url')


class TypeView(ListView):
    template_name = 'type/type_index.html'
    model = TaskType
    context_key = 'type'


class TypeCreate(TemplateView):
    template_name = 'type/type_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TypeForm
        return context

    def post(self, request):
        bound_form = TypeForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('type_url')


