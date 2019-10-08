from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import TypeForm
from webapp.models import TaskType
from .utils import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TypeEdit(UpdateView):
    template_name = 'type/type_edit.html'
    form_class = TypeForm
    model = TaskType
    redirect_url = 'type_url'


class TypeDelete(DeleteView):
    template_name = 'type/type_delete.html'
    model = TaskType
    confirmation = True
    redirect_url = 'type_url'


class TypeView(ListView):
    template_name = 'type/type_index.html'
    model = TaskType
    context_key = 'type'


class TypeCreate(CreateView):
    model = TaskType
    fields = ['type']
    template_name = 'type/type_create.html'
    success_url = reverse_lazy('type_url')


