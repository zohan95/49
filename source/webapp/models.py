from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (('active', 'Активный'), ('inactive', 'Закрытый'))


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
    project = models.ForeignKey('webapp.Project', verbose_name='Проект', related_name='projects', blank=False,
                                null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.summary[:20]


class Project(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    def delete(self):
        self.status = STATUS_CHOICES[1][0]
        self.save()

    def __str__(self):
        return self.summary[:15]


class Team(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь', related_name='team_user')
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name='Проект',
                                   related_name='team_project')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        permissions = (
            ('can_change_team', 'Can Change Team'),
        )
