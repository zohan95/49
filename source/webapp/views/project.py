from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from webapp.models import Project, Task, STATUS_CHOICES
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404


class ProjectView(ListView):
    model = Project
    template_name = 'project/index.html'
    paginate_by = 3
    paginate_orphans = 1
    ordering = ['-date_create']


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
    success_url = reverse_lazy('project_url')


class ProjectDelete(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_url')


class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/create.html'
    fields = ['summary', 'description']
    success_url = reverse_lazy('project_url')
