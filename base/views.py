from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_queryset(self):
        base_qs = super(TaskDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'notes', 'complete']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TaskCreate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'notes', 'complete']
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        base_qs = super(TaskUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        base_qs = super(TaskDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)

def user_settings(request):
    return render(request, 'base/user_settings.html')