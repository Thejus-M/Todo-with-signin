from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Task


class TaskList(ListView):
    model = Task 
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'  # This is to show which all field should be displayed here all
    # else ['fieldname','in alist']
    success_url = reverse_lazy('tasks')
    template_name = "base/Createtask.html"

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__' 
    success_url = reverse_lazy('tasks')
    template_name = "base/Createtask.html"

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = "Delete_Task.html"
