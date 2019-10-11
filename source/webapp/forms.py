from django import forms
from .models import Task, TaskType, TaskStatus, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'task_status', 'task_type', 'project']


class StatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ['type']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['summary', 'description']
