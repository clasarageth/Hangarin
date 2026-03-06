from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Task, SubTask

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_list.html'
    success_url = reverse_lazy('task-list')
    paginate_by = 5


class SubtaskView(ListView):
    model = SubTask
    template_name = 'task_list.html'
    context_object_name = 'subtasks'