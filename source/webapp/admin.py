from django.contrib import admin
from .models import *

admin.site.register(TaskStatus)
admin.site.register(TaskType)
admin.site.register(Task)

