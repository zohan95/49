from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from webapp.models import TaskStatus
from django.urls import reverse_lazy


class StatusView(ListView):
    template_name = 'status/status_index.html'
    model = TaskStatus


class StatusEdit(UpdateView):
    model = TaskStatus
    template_name = 'status/status_edit.html'
    fields = ['status']
    success_url = reverse_lazy('status_url')


class StatusDelete(DeleteView):
    template_name = 'status/status_delete.html'
    model = TaskStatus
    success_url = reverse_lazy('status_url')


class StatusCreate(CreateView):
    model = TaskStatus
    fields = ['status']
    template_name = 'status/status_create.html'
    success_url = reverse_lazy('status_url')



