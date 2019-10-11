# Generated by Django 2.2 on 2019-09-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0002_auto_20190926_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.TaskStatus',
                                    verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.TaskType',
                                    verbose_name='Тип'),
        ),
    ]
