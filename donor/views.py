from django.shortcuts import render, redirect
from django.utils.http import urlencode
from django.contrib import messages
from child.models import Child
from .forms import DonorForm, DonationForm
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import RegistrationView, GroupRequiredMixin, DonorsGroupRequiredMixin
import random
from datetime import date
from .models import Donor, Donation

from django.views.generic import (
    View,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
)

# Create your views here.
class DonorIndexView(TemplateView):
    template_name = 'donor/donation_choices.html'

    def get(self, request):
        if self.request.user.is_authenticated:
            if (self.request.user.is_superuser | self.request.user.is_staff):
                return redirect(reverse('donor:donor-list'))
            # elif self.request.user.groups.filter(name='donors').exists():
            #     print("user is in donors group")
            #     return redirect(reverse('donor:donor-home'))
        return super(DonorIndexView,self).get(request)


class DonationCreateView(LoginRequiredMixin, DonorsGroupRequiredMixin, CreateView):
    template_name = 'donor/donation_create.html'
    form_class = DonationForm
    group_required = [u'donors']

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        print("DonationCreateView: Inside get_initial")
        print("GET next is:")
        print(self.request.GET.get('next'))
        initial = super(DonationCreateView, self).get_initial()
        initial['sponsorship_amount'] = self.request.GET.get('sponsorship_amount')
        initial['expiry_date'] = date.today().replace(year=date.today().year+1)
        return initial

    def form_valid(self, form):
        instance = form.save(commit=False)
        #like a pre_save
        print("DonationCreateView:Inside form_valid")
        print(self.request.user.donor)
        instance.donor=self.request.user.donor
        def child_table_not_empty(self):
            has_child = False
            try:
                has_child = (Child.objects.all().exists())
            except Child.DoesNotExist:
                print("Child table is empty")
            return has_child
        if child_table_not_empty(self):
            print("Child has at least one record")
            instance.child = Child.objects.get(pk=random.randint(1,Child.objects.last().pk))
            return super(DonationCreateView, self).form_valid(form)
        else:
            messages.error(self.request, "Oops!! There are no children in our database at this time. Please click on <label> CONTACT </label> to send us a message.")
            # Future enhancement: override form_invalid to perform error handling for empty child table scenario
            return super(DonationCreateView, self).form_invalid(form)
        # instance.save()
        # like a post_save. instance.save() is not needed as we are going to call form_valid again below ehich does the save() and more...


    def render_to_response(self, context):
        def user_has_donor_profile(self):
            has_donor = False
            try:
                has_donor = (self.request.user.donor is not None)
            except Donor.DoesNotExist:
                pass
            return has_donor
        print("DonationCreateView: Inside render_to_response before")
        print(self.request.path)
        print("GET next is:")
        print(self.request.GET.get('next'))
        print("POST next is:")
        print(self.request.POST.get('next'))
        if not user_has_donor_profile(self):
            path = reverse('donor:donor-create') #, kwargs={'question_id': 123})
            params = urlencode({'next': '/donor/donation?sponsorship_amount=25'})
            url = "%s?%s" % (path, params)
            print(url)
            return redirect(url)
        print("DonationCreateView: Inside render_to_response after")
        # next='/donor/donation?sponsorship_amount=25'
        return super(DonationCreateView, self).render_to_response(context)

class DonationDetailView(DetailView):
    template_name = 'donor/donation_detail.html'
    queryset = Donation.objects.all()
    def get_queryset(self):
        queryset = super(DonationDetailView, self).get_queryset()
        # queryset = Donor.objects.filter(donor_user__id__iexact=self.request.user.id)
        # if (self.request.user.is_superuser | self.request.user.is_staff):
        queryset = Donation.objects.all()
        # queryset = self.request.user.donor
        return queryset
    # def get_object(self, queryset=None):
    #     obj = super(DonorDetailView, self).get_object(queryset=queryset)
    #     if (self.request.user.is_superuser | self.request.user.is_staff):
    #         self.obj=obj
    #     else:
    #         obj = self.request.user.donor
    #     print('inside get_object, obj is:')
    #     print(obj)
    #     return obj

class DonorUserRegistrationView(RegistrationView):
    model = Donor
    def form_valid(self, form):
        super(DonorUserRegistrationView, self).form_valid(form)
        donors_group, created = Group.objects.get_or_create(name='donors')
        print('inside DonorUserRegistrationView: form_valid ')
        # print('template_name: %s' % super.template_name)
        print('template_name is: %s' % self.template_name)
        print("username is: %s" % self.username)
        print("user is: ")
        print(self.user)
        self.user.groups.add(donors_group)
        # print(help(DonorUserRegistrationView))
        return redirect(reverse('donor:donor-create'), user = self.user)

class DonorCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    template_name = 'donor/donor_create.html'
    form_class = DonorForm
    group_required = [u'donors', u'admin']
    # html_var = 'Donor'
    # login_url='/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        #like a pre_save
        instance.donor_user=self.request.user
        print('Inside DonorCreateView - form_valid, GET next is:')
        print(self.request.GET.get('next'))
        print('Inside DonorCreateView - form_valid, POST next is:')
        print(self.request.POST.get('next'))
        print(self.request.POST.get('next') is not None)
        # instance.save()
        # like a post_save. instance.save() is not needed as we are going to call form_valid again below ehich does the save() and more...
        return super(DonorCreateView, self).form_valid(form)

    def render_to_response(self, context):
        print("inside DonorCreateView render_to_response")
        print(self.request.path)
        print("POST is:")
        print(self.request.POST)
        print("GET is:")
        print(self.request.GET)
        return super(DonorCreateView, self).render_to_response(context)

    def get_success_url(self):
        print('Inside DonorCreateView - get_success_url, GET is:')
        print(self.request.GET.get('next'))
        print('Inside DonorCreateView - get_success_url, POST is:')
        POST_next = self.request.POST.get('next')
        def post_param_next_is_empty():
            print("inside post_param_next_is_empty function")
            print('POST_next:')
            print(POST_next)
            print('POST_next is None')
            print(POST_next is None)
            print('POST_next.strip():')
            print(POST_next.strip())
            print("POST_next.strip() or (POST_next is None):")
            print(POST_next.strip() or (POST_next is None))
            return (POST_next.strip() or (POST_next is None))

        print("post_param_next_is_empty:")
        print(post_param_next_is_empty())
        # if not post_param_next_is_empty():
        if POST_next.strip():
            return '/donor/donation?sponsorship_amount=25'
        return super(DonorCreateView, self).get_success_url()

class DonorDetailView(DetailView):
    template_name = 'donor/donor_detail.html'
    queryset = Donor.objects.all()
    # def get_queryset(self):
    #     queryset = super(DonorDetailView, self).get_queryset()
    #     # queryset = Donor.objects.filter(donor_user__id__iexact=self.request.user.id)
    #     # if (self.request.user.is_superuser | self.request.user.is_staff):
    #     queryset = Donor.objects.all()
    #     # queryset = self.request.user.donor
    #     return queryset
    def get_object(self, queryset=None):
        obj = super(DonorDetailView, self).get_object(queryset=queryset)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            self.obj=obj
        else:
            obj = self.request.user.donor
        print('inside get_object, obj is:')
        print(obj)
        return obj


class DonorListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    template_name = 'donor/donor_list.html'
    group_required = [u'admin']
    queryset = Donor.objects.all()

class DonorUpdateView(UpdateView):
    template_name = 'donor/donor_create.html'
    form_class = DonorForm
    queryset = Donor.objects.all()

    def get_object(self, queryset=None):
        obj = super(DonorUpdateView, self).get_object(queryset=queryset)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            self.obj=obj
        else:
            obj = self.request.user.donor
        print('inside get_object, obj is:')
        print(obj)
        return obj


class DonorDeleteView(DeleteView):
    template_name = 'donor/donor_delete.html'
    queryset = Donor.objects.all()

    def get_object(self, queryset=None):
        obj = super(DonorDeleteView, self).get_object(queryset=queryset)
        if (self.request.user.is_superuser | self.request.user.is_staff):
            self.obj=obj
        else:
            obj = self.request.user.donor
        print('inside get_object, obj is:')
        print(obj)
        return obj

    def get_success_url(self):
        return reverse('donor:donor-list')
