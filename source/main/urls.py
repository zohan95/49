"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *

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
    path('status/edit/<int:pk>', StatusEdit.as_view(), name='status_edit_url'),
    path('status/delete/<int:pk>/', StatusDelete.as_view(), name='status_delete_url'),
    path('type/edit/<int:pk>', TypeEdit.as_view(), name='type_edit_url'),
    path('type/delete/<int:pk>/', TypeDelete.as_view(), name='type_delete_url'),
    path('type/create/', TypeCreate.as_view(), name='type_create_url'),
]
