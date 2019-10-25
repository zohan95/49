from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from webapp.forms import TypeForm
from webapp.models import TaskType
from django.urls import reverse_lazy


class TypeEdit(UpdateView):
    template_name = 'type/type_edit.html'
    model = TaskType
    fields = ['type']
    success_url = reverse_lazy('webapp:type_url')


class TypeDelete(DeleteView):
    template_name = 'type/type_delete.html'
    model = TaskType
    success_url = reverse_lazy('webapp:type_url')


class TypeView(ListView):
    template_name = 'type/type_index.html'
    model = TaskType


class TypeCreate(CreateView):
    model = TaskType
    fields = ['type']
    template_name = 'type/type_create.html'
    success_url = reverse_lazy('webapp:type_url')
