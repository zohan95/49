from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import SimpleSearchForm
from webapp.models import Task, STATUS_CHOICES, Team, Project
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required


class TaskDetails(DetailView):
    template_name = 'task/details.html'
    model = Task


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['summary', 'description', 'task_status', 'task_type', 'project']
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('webapp:main_url')
    permission_required = 'webapp.add_task'

    def form_valid(self, form):
        project = form.cleaned_data['project']
        team = Team.objects.filter(user_id=self.request.user.id, project_id=project.id)

        if project.status == STATUS_CHOICES[0][0]:
            if team:
                return super().form_valid(form)
            else:
                errors = form._errors.setdefault("project", ErrorList())
                errors.append(u"Вы не в команде!!!")
                return render(self.request, 'task/task_create.html', {'form': form})
        else:
            errors = form._errors.setdefault("project", ErrorList())
            errors.append(u"Вы выбрали неактивный проект!!!")
            return render(self.request, 'task/task_create.html', {'form': form})



class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_edit.html'
    fields = ['summary', 'description', 'task_status', 'task_type', 'project']
    success_url = reverse_lazy('webapp:main_url')
    permission_required = 'webapp.change_task'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        team = Team.objects.filter(user_id=self.request.user.id, project_id=task.project.id)
        if task.project.status == STATUS_CHOICES[0][0] and team:
            return super().get(self, request, *args, **kwargs)
        else:
            raise PermissionDenied()


class TaskDelete(LoginRequiredMixin, DeleteView):
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('webapp:main_url')
    model = Task
    permission_required = 'webapp.delete_task'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        team = Team.objects.filter(user_id=self.request.user.id, project_id=task.project.id)
        if task.project.status == STATUS_CHOICES[0][0] and team:
            return super().get(self, request, *args, **kwargs)
        else:
            raise PermissionDenied()


class MainPage(ListView):
    template_name = 'task/index.html'
    model = Task
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
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
