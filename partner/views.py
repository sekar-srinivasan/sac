from django.shortcuts import render
from project.models import Project
from child.models import Child
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView
)

# Create your views here.

class PartnerView(LoginRequiredMixin, ListView):
    template_name = 'partner/partner.html'
    def get_queryset(self):
        print('user printed from PartnerView is: ')
        print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = self.request.user.project_set.all()
        # queryset = Project.objects.all()
        print(queryset)
        # queryset = Child.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Project.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PartnerView, self).get_context_data(**kwargs)
        context['child_list'] = self.request.user.project_children.all()
        # And so on for more models
        return context
