from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm
from datetime import timedelta 
from django.utils import timezone

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
        context["total_tasks"] = Task.objects.count()

        today = timezone.now().date()

        # start of week (Monday)
        start_week = today - timedelta(days=today.weekday())

        # end of week (Sunday)
        end_week = start_week + timedelta(days=6)

        count = Task.objects.filter(
            deadline__range=(start_week, end_week)
        ).count()

        tasks_today = Task.objects.filter(
            deadline__date=today
        ).count()

        context["tasks_today"] = tasks_today

        context["tasks_this_week"] = count

        completed_tasks = Task.objects.filter(
            status='Completed'
        ).count()

        context["completed_tasks"] = completed_tasks

        return context
    
        # today = timezone.now().date()
        # count = (
        #     OrgMember.objects.filter(
        #         date_joined__year=today.year
        #     )
        #     .values("student")
        #     .distinct()
        #     .count()
        # )
    
        # context["students_joined_this_year"] = count
        # return context



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

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks_del.html'
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

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtasks_del.html'
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

class NotesDeleteView(DeleteView):
    model = Note
    template_name = 'notes_del.html'
    success_url = reverse_lazy('notes-list')

class CategoriesListView(ListView):
    model = Category
    template_name = 'Categories_list.html'
    context_object_name = 'categories'

class CategoriesCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('categories-list')

class CategoriesUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories_form.html'
    success_url = reverse_lazy('categories-list')

class CategoriesDeleteView(DeleteView):
    model = Category
    template_name = 'categories_del.html'
    success_url = reverse_lazy('categories-list')

class PrioritiesListView(ListView):
    model = Priority
    template_name = 'priorities_list.html'
    context_object_name = 'priorities'

class PrioritiesCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priorities_form.html'
    success_url = reverse_lazy('priorities-list')

class PrioritiesUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priorities_form.html'
    success_url = reverse_lazy('priorities-list')

class PrioritiesDeleteView(DeleteView):
    model = Priority
    template_name = 'priorities_del.html'
    success_url = reverse_lazy('priorities-list')