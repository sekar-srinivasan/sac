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

def index_view(request, *args, **kwargs):
    #print(args, kwargs)
    #print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "index.html", {})

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
        # like a post_save. This is not needed as we are going to call form_valid again below ehich does the save() and more...
        return super(DonorCreateView, self).form_valid(form)

class DonorDetailView(DetailView):
    template_name = 'donor/donor_detail.html'
    queryset = Donor.objects.all()
    # def get_queryset(self):
    #     return Donor.objects.filter(owner=self.request.user)

class DonorListView(LoginRequiredMixin, ListView):
    template_name = 'donor/donor_list.html'
    queryset = Donor.objects.all()

class DonorUpdateView(UpdateView):
    template_name = 'donor/donor_create.html'
    form_class = DonorForm
    queryset = Donor.objects.all()
    # def get_queryset(self):
    #     return Donor.objects.filter(owner=self.request.user)

class DonorDeleteView(DeleteView):
    template_name = 'donor/donor_delete.html'
    queryset = Donor.objects.all()
    # def get_queryset(self):
    #     return Donor.objects.filter(owner=self.request.user)


    def get_success_url(self):
        return reverse('donor:donor-list')
