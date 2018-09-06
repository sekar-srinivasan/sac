from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
from django.urls import reverse

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)

# Create your views here.

class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm

class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    queryset = Project.objects.all()
    # def get_queryset(self):
    #     return Project.objects.filter(owner=self.request.user)

class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    queryset = Project.objects.all()

class ProjectUpdateView(UpdateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    queryset = Project.objects.all()
    # def get_queryset(self):
    #     return Project.objects.filter(owner=self.request.user)

class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    queryset = Project.objects.all()
    # def get_queryset(self):
    #     return Project.objects.filter(owner=self.request.user)


    def get_success_url(self):
        return reverse('project:project-list')
