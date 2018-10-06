from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

class SACLoginView(LoginView):
    def get_success_url(self, **kwargs):
        print('Inside SACLoginView: get_success_url:')
        print('does the user belong to project_partners group?')
        print(self.request.user)
        print(self.request.user.groups.filter(name='project_partners').exists())
        if self.request.user.groups.filter(name='project_partners').exists():
            print("user is in project_partners group")
            return reverse('partner:partner')
        elif self.request.user.groups.filter(name='donors').exists():
            print("user is in donors group")
            return reverse('donor:donor-list')
        return super(SACLoginView, self).get_success_url(**kwargs)


class RegistrationView(FormView):
    form_class = UserCreationForm
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
