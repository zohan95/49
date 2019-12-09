from django.shortcuts import render

from rest_framework import viewsets

from api_v2.permissions import CustomDjangoModelPermission
from webapp.models import Project, Task

from api_v2.serializers import ProjectSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, DjangoModelPermissions


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (DjangoModelPermissions,)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (DjangoModelPermissions,)
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()

