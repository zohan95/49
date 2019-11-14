from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.timezone import now
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


from webapp.forms import SimpleSearchForm, ProjectForm
from webapp.models import Project, Task, STATUS_CHOICES, Team
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


class ProjectDetails(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project/details.html'

    def get_context_data(self, **kwargs):
        project = kwargs.get('object')
        tasks = Task.objects.filter(project=project).order_by('date_create')
        context = super().get_context_data(**kwargs)
        paginator = Paginator(tasks, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        slaves = Team.objects.filter(project_id=project).filter(date_end=None).order_by('-date_start')
        seen = []
        keep = []
        for o in slaves:
            if seen.count(o.user_id) == 0:
                keep.append(o)
                seen.append(o.user_id)
        context['slaves'] = keep

        context['paginator'] = paginator
        context['page_obj'] = page
        context['is_paginated'] = page.has_other_pages()
        context['tasks'] = page.object_list
        return context


class ProjectEdit(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/edit.html'
    fields = ['summary', 'description']
    success_url = reverse_lazy('webapp:project_url')

    def get_context_data(self, **kwargs):
        if self.request.user.has_perm('webapp.change_project') or self.request.user.has_perm('webapp.can_change_team'):
            context = super().get_context_data(**kwargs)
            context['form'] = ProjectForm(instance=self.object)
            users = User.objects.all()
            slaves = Team.objects.filter(project_id=self.object).filter(date_end=None).order_by('-date_start')
            seen = []
            keep = []
            for o in slaves:
                if seen.count(o.user_id) == 0:
                    keep.append(o)
                    seen.append(o.user_id)
            list_users = []
            for i in users:
                list_users.append(i.username)
            print(list_users)
            for i in keep:
                if str(i.user_id) in list_users:
                    list_users.remove(str(i.user_id))
            context['active_users'] = keep
            context['list_users'] = list_users
            return context
        else:
            raise PermissionDenied()

    def form_valid(self, form, *args, **kwargs):
        a = super().form_valid(form)
        users = self.request.POST.getlist('user_list')
        del_users = self.request.POST.getlist('active_users')
        for i in del_users:
            obj = Team.objects.get(pk=i)
            obj.date_end = now()
            obj.save()
        for i in users:
            Team(project_id=self.object, user_id=User.objects.get(username=i), date_start=now()).save()
        return a


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('webapp:project_url')
    permission_required = 'webapp.delete_project'


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project/create.html'
    fields = ['summary', 'description']
    permission_required = 'webapp.add_project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        list_users = []
        cur_user = self.request.user.username
        for i in users:
            list_users.append(i.username)
        list_users.remove(cur_user)
        context['list_users'] = list_users
        return context

    def get_success_url(self):
        team = Team()
        team.project_id = self.object
        team.user_id = self.request.user
        team.date_start = now()
        team.save()
        return reverse_lazy('webapp:project_url')

    def form_valid(self, form, *args, **kwargs):
        a = super().form_valid(form)
        users = self.request.POST.getlist('user_list')
        for i in users:
            Team(project_id=self.object, user_id=User.objects.get(username=i), date_start=now()).save()
        return a
