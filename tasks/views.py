from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'



class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task 
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class SubTaskListView(ListView):
    model = SubTask
    template_name = 'subtasks_list.html'
    context_object_name = 'subtasks'

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtasks_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtasks_form.html'
    success_url = reverse_lazy('subtask-list')

class NotesListView(ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes'

class NotesCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('notes-list')

class NotesUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('notes-list')

class CategoriesListView(ListView):
    model = Category
    template_name = 'Categories_list.html'
    context_object_name = 'categories'

class CategoriesUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('categories-list')

class PrioritiesListView(ListView):
    model = Priority
    template_name = 'priorities_list.html'
    context_object_name = 'priorities'

class PrioritiesUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priorities_form.html'
    success_url = reverse_lazy('priorities-list')