from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from webapp.forms import SimpleSearchForm
from webapp.models import Project, Task, STATUS_CHOICES
from django.urls import reverse_lazy


class ProjectView(ListView):
    model = Project
    template_name = 'project/index.html'
    ordering = ['-date_create']

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectDetails(DeleteView):
    model = Project
    template_name = 'project/details.html'

    def get_context_data(self, **kwargs):
        project = kwargs.get('object')
        tasks = Task.objects.filter(project=project).order_by('date_create')
        context = super().get_context_data(**kwargs)
        paginator = Paginator(tasks, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['is_paginated'] = page.has_other_pages()
        context['tasks'] = page.object_list
        return context


class ProjectEdit(UpdateView):
    model = Project
    template_name = 'status/status_edit.html'
    fields = ['summary', 'description']
    success_url = reverse_lazy('webapp:project_url')


class ProjectDelete(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('webapp:project_url')


class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/create.html'
    fields = ['summary', 'description']
    success_url = reverse_lazy('webapp:project_url')