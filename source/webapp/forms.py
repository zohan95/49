from django import forms
from .models import Task, TaskType, TaskStatus


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'task_status', 'task_type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = ['type']


