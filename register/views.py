from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from register.forms import RegistrationForm
# Create your views here.


def register(request):
    variables = {}
    if request.user.is_authenticated:
        HttpResponseRedirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)



    else:
        form = RegistrationForm()

    variables['form'] = form

    return render(request,'register.html',variables)

