from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy


# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True

    return render(request, 'app_login/signup.html', context={'title': 'Signup Form from here', 'form': form})
