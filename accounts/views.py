from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index_view(request, *args, **kwargs):
    #print(args, kwargs)
    #print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "index.html", {})

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/sac/")
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, "registration/register.html", context)
