from django import forms
from django.contrib.auth.models import User

from webapp.models import Project


class ProjectCreateForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['summary', 'description']

