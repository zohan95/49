# Generated by Django 2.2 on 2019-09-26 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('description',
                 models.TextField(blank=True, max_length=2000, null=True, verbose_name='Полное описание')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('taks_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.TaskStatus')),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.TaskType')),
            ],
        ),
    ]
