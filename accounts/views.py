from django.shortcuts import render, redirect
from django.utils.http import urlencode
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from accounts.forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        print("Inside CustomLoginRequiredMixin")
        print(self.request.session.items())
        print("self.request.GET.get('sponsorship_amount')")
        print(self.request.GET.get('sponsorship_amount'))
        print("self.kwargs.get('project_pk')")
        print(self.kwargs.get('project_pk'))
        print("self.kwargs.get('child_pk')")
        print(self.kwargs.get('child_pk'))
        if self.request.GET.get('sponsorship_amount'):
            self.request.session['sponsorship_amount'] = self.request.GET.get('sponsorship_amount')
            messages.info(self.request, "Thank you for deciding to sponsor $" + self.request.session['sponsorship_amount'] + ". You will see your assigned child after signing in.")
        print(self.request.session.items())
        if 'sponsorship_amount' in self.request.session:
            if self.kwargs.get('project_pk'):
                print(" inside if self.kwargs.get('project_pk')")
                print(self.kwargs.get('project_pk'))
                self.request.session['project_pk'] = self.kwargs.get('project_pk')
            elif self.kwargs.get('child_pk'):
                print(" inside if self.kwargs.get('child_pk')")
                print(self.kwargs.get('child_pk'))
                self.request.session['child_pk'] = self.kwargs.get('child_pk')
        print(self.request.session.items())
        return super(CustomLoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class GroupRequiredMixin(object):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif (self.request.user.is_superuser | self.request.user.is_staff):
            return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            user_groups = []
            for group in request.user.groups.values_list('name', flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)

class PartnerGroupRequiredMixin(GroupRequiredMixin):
    """
        group_required - list of strings, required param
    """

    group_required = [u'project_partners']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif (self.request.user.is_superuser | self.request.user.is_staff):
            return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
        elif self.request.user.groups.filter(name='project_partners').exists():
            return super(PartnerGroupRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            path = reverse('accounts:login') #, kwargs={'question_id': 123})
            params = urlencode({'next': reverse('partner:partner-dashboard')})
            url = "%s?%s" % (path, params)
            print(url)
            return redirect(url)
class AdminGroupRequiredMixin(GroupRequiredMixin):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif (self.request.user.is_superuser | self.request.user.is_staff):
            return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            path = reverse('accounts:login') #, kwargs={'question_id': 123})
            params = urlencode({'next': reverse('partner:partner-dashboard')})
            url = "%s?%s" % (path, params)
            print(url)
            return redirect(url)
class DonorsGroupRequiredMixin(GroupRequiredMixin):
    """
        group_required - list of strings, required param
    """

    group_required = [u'donors']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif (self.request.user.is_superuser | self.request.user.is_staff):
            return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
        elif self.request.user.groups.filter(name='donors').exists():
            return super(DonorsGroupRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            path = reverse('accounts:login') #, kwargs={'question_id': 123})
            params = urlencode({'next': reverse('donor:donor-index')})
            url = "%s?%s" % (path, params)
            print(url)
            return redirect(url)

class SACLoginView(LoginView):
    def get_success_url(self, **kwargs):
        print('Inside SACLoginView: get_success_url:')
        if self.request.user.groups.filter(name='project_partners').exists():
            print("user is in project_partners group")
            return reverse('partner:partner-dashboard')
        elif self.request.user.groups.filter(name='donors').exists():
            print("Inside SACLoginView, user is in donors group")
            print(self.request.session.items())
            if 'sponsorship_amount' in self.request.session:
                if 'project_pk' in self.request.session:
                    return reverse('donor:donation-within-project', kwargs={'project_pk': self.request.session['project_pk']})
                else:
                    return reverse('donor:donation')
            else:
                return reverse('donor:donor-index')
        elif (self.request.user.is_superuser | self.request.user.is_staff):
            return reverse('donor:admin-donations-dashboard')

        return super(SACLoginView, self).get_success_url(**kwargs)


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    username = ''
    user = User()

    def form_valid(self, form):
        form.save()
        self.username = form.cleaned_data.get('username')
        print('inside RegistrationView: form_valid ')
        print('template_name: %s' % self.template_name)
        print("username: %s" % self.username)
        raw_password = form.cleaned_data.get('password1')
        self.user = authenticate(username=self.username, password=raw_password)
        login(self.request, self.user)
        # return redirect('/sac/')
        return super(RegistrationView, self).form_valid(form)

    def get_success_url(self):
        return reverse('project:project-list')

def index_view(request, *args, **kwargs):
    #print(args, kwargs)
    #print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "index.html", {})

# def register_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect("/sac/")
#     else:
#         form = UserCreationForm()
#     context = {'form' : form}
#     return render(request, "registration/register.html", context)
