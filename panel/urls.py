"""
URL configuration for panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tasks, name='tasks'),
    path('task/<int:id>', views.task, name='task'),
    path('task/<int:id>/edit', views.task_edit, name='task_edit'),
    path('task/<int:id>/delete', views.task_delete, name='task_delete'),
    path('task/<int:id>/complete', views.task_complete, name='task_complete'),
    path('create-task/', views.create_task, name='create_task'),
]