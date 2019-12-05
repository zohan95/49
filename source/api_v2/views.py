from django.shortcuts import render

from rest_framework import viewsets

from webapp.models import Project, Task

from api_v2.serializers import ProjectSerializer, TaskSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    serializer_class = TaskSerializer

