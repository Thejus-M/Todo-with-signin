from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy



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
