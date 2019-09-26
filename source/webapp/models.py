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
    taks_status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.summary[:20]



