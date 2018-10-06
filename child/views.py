from django.shortcuts import render
from project.models import Project
from .models import Child
from .forms import ChildForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)

# Create your views here.

class ChildCreateView(LoginRequiredMixin, CreateView):
    template_name = 'child/child_create.html'
    form_class = ChildForm
    # html_var = 'Child'
    # login_url='/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        #like a pre_save
        instance.project_partner_user=self.request.user
        project = Project.objects.get(pk=self.kwargs['project_pk'])
        instance.project = project
        #we could also poplulate just the project id as shown below:
        #project_pk = self.kwargs['project_pk']
        # instance.save()
        # like a post_save. instance.save() is not needed as we are going to call form_valid again below ehich does the save() and more...
        return super(ChildCreateView, self).form_valid(form)

class ChildDetailView(DetailView):
    template_name = 'child/child_detail.html'
    def get_queryset(self):
        print('user printed from ChildDetailView is: ')
        print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.project_children.all()
        print(queryset)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset



class ChildListView(LoginRequiredMixin, ListView):
    template_name = 'child/child_list.html'
    # form_class=ChildForm # If there is nothing in this list, need this form to be used while redirecting user to child_create page.
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.project_children.all()
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset



class ChildUpdateView(UpdateView):
    template_name = 'child/child_create.html'
    form_class = ChildForm
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.project_children.all()
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset



class ChildDeleteView(DeleteView):
    template_name = 'child/child_delete.html'
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        queryset = self.request.user.project_children.all()
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('child:child-list')
