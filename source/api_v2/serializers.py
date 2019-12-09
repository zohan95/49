from webapp.models import Project, Task

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    projectz = TaskSerializer(many=True, read_only=True, source='projects')

    class Meta:
        model = Project
        fields = ('summary',  'description', 'status', 'projectz')

