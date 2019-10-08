from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, CreateView
from webapp.forms import StatusForm
from webapp.models import TaskStatus
from .utils import ListView
from django.urls import reverse_lazy


class StatusView(ListView):
    template_name = 'status/status_index.html'
    model = TaskStatus
    context_key = 'status'


class StatusEdit(TemplateView):
    template_name = 'status/status_edit.html'

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
    template_name = 'status/status_delete.html'

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


class StatusCreate(CreateView):
    model = TaskStatus
    fields = ['status']
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('status_url')