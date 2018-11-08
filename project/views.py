from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.urls import reverse
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import RegistrationView, GroupRequiredMixin, PartnerGroupRequiredMixin, AdminGroupRequiredMixin

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)

# Create your views here.
class PartnerUserRegistrationView(RegistrationView):
    model = Project
    def form_valid(self, form):
        # added logic to:
        # 0. call super to call parent's form_valid to create and save user to request
        # 1. get or create project_partners group
        # 2. get or create permission and addit it to the group
        # 2. assign the user to the group
        # 3. populate instance.project_partner_user with this user
        # 5. call the return super... menthod to save the project with new user.
        super(PartnerUserRegistrationView, self).form_valid(form)
        project_partners_group, created = Group.objects.get_or_create(name='project_partners')
        ct = ContentType.objects.get_for_model(Project)

        permission, permission_newly_created = Permission.objects.get_or_create(codename='can_add_modify_child',
                                           name='Can add, remove, modify, delete child',
                                           content_type=ct)
        if not project_partners_group.permissions.filter(name='can_add_modify_child').exists():
            print('adding permission')
            project_partners_group.permissions.add(permission)

        # email = form.cleaned_data['contact_email']
        print('inside PartnerUserRegistrationView: form_valid ')
        # print('template_name: %s' % super.template_name)
        print('template_name is: %s' % self.template_name)
        print("username is: %s" % self.username)
        print("user is: ")
        print(self.user)
        self.user.groups.add(project_partners_group)
        # print(help(PartnerUserRegistrationView))
        return redirect(reverse('project:project-create'), user = self.user)

class ProjectCreateView(LoginRequiredMixin, PartnerGroupRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    # def get_context_data(self, **kwargs):
    #     context = super(ProjectCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        #like a pre_save
        # username = form.cleaned_data['user_name']
        print('Inside ProjectCreateView user is:')
        print(self.request.user)
        # user = User.objects.create_user(username, 'lennon@thebeatles.com', 'johnpassword')
        # instance.project_partner_user = user
        instance.project_partner_user=self.request.user
        # project = Project.objects.get(pk=self.kwargs['pk'])
        # print('pk is %s:' % pk )
        # instance.project = project
        #we could also poplulate just the project id as shown below:
        #project_pk = self.kwargs['project_pk']
        # instance.save()
        # like a post_save. instance.save() is not needed as we are going to call form_valid again below ehich does the save() and more...
        return super(ProjectCreateView, self).form_valid(form)

class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    queryset = Project.objects.all()

class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    # queryset = Project.objects.all()
    def get_queryset(self):
        print("Inside ProjectListView:get_queryset")
        print(self.request.session.items())
        print(self.request.GET.get('sponsorship_amount'))
        if self.request.GET.get('sponsorship_amount'):
            self.request.session['sponsorship_amount'] = self.request.GET.get('sponsorship_amount')
        print(self.request.session.items())
        return Project.objects.all()
        # return Project.objects.filter(owner=self.request.user)

class ProjectUpdateView(LoginRequiredMixin, AdminGroupRequiredMixin, UpdateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    queryset = Project.objects.all()
    # def get_queryset(self):
    #     return Project.objects.filter(owner=self.request.user)

class ProjectDeleteView(LoginRequiredMixin, AdminGroupRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    queryset = Project.objects.all()
    # def get_queryset(self):
    #     return Project.objects.filter(owner=self.request.user)


    def get_success_url(self):
        return reverse('project:project-list')
