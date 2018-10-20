from django.shortcuts import render
from project.models import Project
from .models import Child, Progress
from .forms import ChildForm, ProgressForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import PartnerGroupRequiredMixin, DonorsGroupRequiredMixin, GroupRequiredMixin


from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)

# Create your views here.

class ChildCreateView(LoginRequiredMixin, PartnerGroupRequiredMixin, CreateView):
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

class ChildDetailView(LoginRequiredMixin, PartnerGroupRequiredMixin, DetailView):
    template_name = 'child/child_detail.html'
    def get_queryset(self):
        print('user printed from ChildDetailView is: ')
        print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.partner_user_children.all()
        print(queryset)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset



class ChildListView(LoginRequiredMixin, PartnerGroupRequiredMixin, ListView):
    template_name = 'child/child_list.html'
    # form_class=ChildForm # If there is nothing in this list, need this form to be used while redirecting user to child_create page.
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.partner_user_children.all()
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset



class ChildUpdateView(LoginRequiredMixin, PartnerGroupRequiredMixin, UpdateView):
    template_name = 'child/child_create.html'
    form_class = ChildForm
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.partner_user_children.all()
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset



class ChildDeleteView(LoginRequiredMixin, PartnerGroupRequiredMixin, DeleteView):
    template_name = 'child/child_delete.html'
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        queryset = self.request.user.partner_user_children.all()
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Child.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('child:child-list')

        # progress table CRUD
class ProgressCreateView(LoginRequiredMixin, PartnerGroupRequiredMixin, CreateView):
    template_name = 'child/progress_create.html'
    form_class = ProgressForm
    # html_var = 'Child'
    # login_url='/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        #like a pre_save
        # instance.project_partner_user=self.request.user
        instance.child = Child.objects.get(pk=self.kwargs['child_pk'])
        #we could also poplulate just the project id as shown below:
        #project_pk = self.kwargs['project_pk']
        # instance.save()
        # like a post_save. instance.save() is not needed as we are going to call form_valid again below ehich does the save() and more...
        return super(ProgressCreateView, self).form_valid(form)

class ProgressDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    template_name = 'child/progress_detail.html'
    group_required = [u'donors', u'project_partners' ]
    def get_queryset(self):
        print('user printed from ProgressDetailView is: ')
        print(self.request.user)
        child = Child.objects.get(pk=self.kwargs['child_pk'])

        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = child.progress_set.all()
        print(queryset)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        # if (self.request.user.is_superuser | self.request.user.is_staff):
        #     queryset = Progress.objects.all()
        return queryset



class ProgressListView(LoginRequiredMixin, PartnerGroupRequiredMixin, ListView):
    template_name = 'child/progress_list.html'
    child = None
    # form_class=ChildForm # If there is nothing in this list, need this form to be used while redirecting user to child_create page.
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        self.child = Child.objects.get(pk=self.kwargs['child_pk'])
        queryset = self.child.progress_set.all()
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        # if (self.request.user.is_superuser | self.request.user.is_staff):
        #     queryset = Progress.objects.all()
        return queryset
    def get_context_data(self, *args, **kwargs):
        context = super(ProgressListView, self).get_context_data(*args, **kwargs)
        context['child'] = self.child
        return context


class ProgressUpdateView(LoginRequiredMixin, PartnerGroupRequiredMixin, UpdateView):
    template_name = 'child/progress_create.html'
    form_class = ProgressForm
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        child = Child.objects.get(pk=self.kwargs['child_pk'])
        queryset = child.progress_set.all()
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        # if (self.request.user.is_superuser | self.request.user.is_staff):
        #     queryset = Progress.objects.all()
        return queryset



class ProgressDeleteView(LoginRequiredMixin, PartnerGroupRequiredMixin, DeleteView):
    template_name = 'child/progress_delete.html'
    def get_queryset(self):
        # print('user printed from ChildListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        child = Child.objects.get(pk=self.kwargs['child_pk'])
        queryset = child.progress_set.all()
        # if (self.request.user.is_superuser | self.request.user.is_staff):
        #     queryset = Progress.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('child:progress-list')
