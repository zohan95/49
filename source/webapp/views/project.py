from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from webapp.models import Project
from django.urls import reverse_lazy


class ProjectView(ListView):
    model = Project
    template_name = 'project/index.html'
    paginate_by = 3
    paginate_orphans = 1


class ProjectDetails(DeleteView):
    model = Project
    template_name = 'project/details.html'


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

