"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tasks import views
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from tasks.views import TaskListView, TaskCreateView, TaskUpdateView,TaskDeleteView,PrioritiesDeleteView, CategoriesDeleteView, NotesDeleteView,SubTaskDeleteView, SubTaskListView, SubTaskUpdateView, NotesListView, NotesUpdateView, CategoriesListView, CategoriesCreateView, CategoriesUpdateView, PrioritiesListView, NotesCreateView, PrioritiesUpdateView, SubTaskCreateView, PrioritiesCreateView
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', TaskListView.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('subtasks/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<pk>', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),
    path('notes_list/', NotesListView.as_view(), name='notes-list'),
    path('notes_list/add', NotesCreateView.as_view(), name='notes-add'),
    path('notes_list/<pk>', NotesUpdateView.as_view(), name='notes-update'),
    path('notes_list/<pk>/delete', NotesDeleteView.as_view(), name='notes-delete'),
    path('categories_list/', CategoriesListView.as_view(), name='categories-list'),
    path('categories_list/add', CategoriesCreateView.as_view(), name='categories-add'),
    path('categories_list/<pk>', CategoriesUpdateView.as_view(), name='categories-update'),
    path('categories_list/<pk>/delete', CategoriesDeleteView.as_view(), name='categories-delete'),
    path('priorities_list/', PrioritiesListView.as_view(), name='priorities-list'),
    path('priorities_list/add', PrioritiesCreateView.as_view(), name='priorities-add'),
    path('priorities_list/<pk>', PrioritiesUpdateView.as_view(), name='priorities-update'),
    path('priorities_list/<pk>/delete', PrioritiesDeleteView.as_view(), name='priorities-delete'),

]
