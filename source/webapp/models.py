from django.db import models


class TaskStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.status


class TaskType(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тип')

    def __str__(self):
        return self.type


class Task(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Краткое описание')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Полное описание')
    task_status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, verbose_name='Статус')
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT, verbose_name='Тип')
    date_create = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('webapp.Project', verbose_name='Проект', related_name='projects', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.summary[:20]


class Project(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


