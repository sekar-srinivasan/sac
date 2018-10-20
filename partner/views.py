from django.shortcuts import render
from django.contrib import messages
from project.models import Project
from child.models import Child
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import PartnerGroupRequiredMixin
from django.views.generic import (
    ListView
)

# Create your views here.

class PartnerView(LoginRequiredMixin, PartnerGroupRequiredMixin, ListView):
    template_name = 'partner/partner_dashboard.html'
    # group_required = [u'project_partners']
    def get_queryset(self, *args, **kwargs):
        print('user printed from PartnerView is: ')
        print(self.request.user)
        print(self.kwargs)
        print(self.args)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Project.objects.all()
        else:
            queryset = self.request.user.project_set.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerView, self).get_context_data(*args, **kwargs)
        queryset = self.get_queryset(*args, **kwargs)
        print(queryset.exists())
        if queryset.exists():
            project_pk = self.kwargs.get('project_pk', self.get_queryset(*args, **kwargs).first().pk)
            print(self.kwargs)
            print(project_pk)
            context['child_list'] = self.get_queryset(*args, **kwargs).get(pk=project_pk).project_children.all()
        # context['child_list'] = self.request.user.partner_user_children.all()
        # context['project_list'] = self.request.user.project_set.all()
        # context['child_list'] = Project.objects.get(pk=project_pk).project_children.all()
        # or use self.kwargs.get('project_pk')
        # And so on for more models
        # else:
        #     messages.error(self.request, "Please start adding your projects by clicking on <label> ADD PROJECT </label>.")
        return context
