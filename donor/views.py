from django.shortcuts import render
from .models import Donor
from .forms import DonorForm
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

class DonorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'donor/donor_create.html'
    form_class = DonorForm
    # html_var = 'Donor'
    # login_url='/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        #like a pre_save
        instance.created_by=self.request.user
        # instance.save()
        # like a post_save. instance.save() is not needed as we are going to call form_valid again below ehich does the save() and more...
        return super(DonorCreateView, self).form_valid(form)

class DonorDetailView(DetailView):
    template_name = 'donor/donor_detail.html'
    def get_queryset(self):
        # print('user printed from DonorDetailView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = Donor.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Donor.objects.all()
        return queryset



class DonorListView(LoginRequiredMixin, ListView):
    template_name = 'donor/donor_list.html'
    form_class=DonorForm # If there is nothing in this list, need this form to be used while redirecting user to donor_create page.
    def get_queryset(self):
        # print('user printed from DonorListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = Donor.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Donor.objects.all()
        return queryset



class DonorUpdateView(UpdateView):
    template_name = 'donor/donor_create.html'
    form_class = DonorForm
    def get_queryset(self):
        # print('user printed from DonorListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = Donor.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Donor.objects.all()
        return queryset



class DonorDeleteView(DeleteView):
    template_name = 'donor/donor_delete.html'
    def get_queryset(self):
        # print('user printed from DonorListView is: ')
        # print(self.request.user)
        # print(self.request.user.is_staff)
        # print(self.request.user.is_superuser)
        queryset = Donor.objects.filter(created_by__id__iexact=self.request.user.id)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            queryset = Donor.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('donor:donor-list')
