from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, CreateView
from webapp.forms import StatusForm
from webapp.models import TaskStatus
from .utils import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


class StatusView(ListView):
    template_name = 'status/status_index.html'
    model = TaskStatus
    context_key = 'status'


class StatusEdit(UpdateView):
    model = TaskStatus
    template_name = 'status/status_edit.html'
    form_class = StatusForm
    redirect_url = 'status_url'


class StatusDelete(DeleteView):
    template_name = 'status/status_delete.html'
    model = TaskStatus
    redirect_url = 'status_url'


class StatusCreate(CreateView):
    model = TaskStatus
    fields = ['status']
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('status_url')



