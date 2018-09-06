from django.shortcuts import render
from django.views.generic import ListView
from donor.models import Donor
from project.models import Project
from itertools import chain

# Create your views here.
class SearchView(ListView):
    template_name = 'search/search_list.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = self.request.GET.get('q' or None)
        if query is not None:
            donor_results = Donor.objects.search(query=query)
            project_results = Project.objects.search(query=query)
            queryset_chain = chain (
                donor_results,
                project_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True
                        )
            self.count = len(qs)
            return qs

            return Donor.objects.search(query=query)
        return Donor.objects.none()
