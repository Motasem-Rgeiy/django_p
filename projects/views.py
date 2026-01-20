from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from . import models , forms
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class projectListView(LoginRequiredMixin,ListView):
    model = models.project
    template_name = 'project/list.html'
    paginate_by = 6
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q' , None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin ,CreateView):
    model = models.project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(LoginRequiredMixin ,UpdateView):
    model = models.project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    

class ProjectDeleteView(LoginRequiredMixin ,DeleteView):
    model = models.project
    template_name = 'project/delete.html'
    def get_success_url(self):
        return reverse_lazy('project_list')
    


class TaskCreateView(LoginRequiredMixin , CreateView):
    model = models.Task
    fields = ['project','description']
    http_method_names = ['post']
    template_name = 'project/task.html'
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])
    

class TaskDeleteView(LoginRequiredMixin , DeleteView):
    model = models.Task
    template_name = 'project/delete.html'

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])