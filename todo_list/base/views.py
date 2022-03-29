from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Task


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    


class TaskList(LoginRequiredMixin,ListView):
    model = Task 
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False)
        return context
    


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')
    template_name = "base/Createtask.html"
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_vaild(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')
    template_name = "base/Createtask.html"

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = "base/Delete_Task.html"

