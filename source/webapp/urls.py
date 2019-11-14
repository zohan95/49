from django.contrib import admin
from django.urls import path
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main_url'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task_details_url'),
    path('task/create/', TaskCreate.as_view(), name='task_create_url'),
    path('task/edit/<int:pk>/', TaskEdit.as_view(), name='task_edit_url'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete_url'),
    path('status/', StatusView.as_view(), name='status_url'),
    path('type/', TypeView.as_view(), name='type_url'),
    path('type/create/', TypeCreate.as_view(), name='type_create_url'),
    path('status/create/', StatusCreate.as_view(), name='status_create_url'),
    path('status/edit/<int:pk>/', StatusEdit.as_view(), name='status_edit_url'),
    path('status/delete/<int:pk>/', StatusDelete.as_view(), name='status_delete_url'),
    path('type/edit/<int:pk>', TypeEdit.as_view(), name='type_edit_url'),
    path('type/delete/<int:pk>/', TypeDelete.as_view(), name='type_delete_url'),
    path('project/', ProjectView.as_view(), name='project_url'),
    path('project/<int:pk>/', ProjectDetails.as_view(), name='project_details_url'),
    path('project/edit/<int:pk>/', ProjectEdit.as_view(), name='project_edit_url'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='project_delete_url'),
    path('project/create/', ProjectCreate.as_view(), name='project_create_url'),
    path('project/user/delete/<str:user_1>/<int:id>/', TeamUserDel.as_view(), name='team_user_del_url')
]
