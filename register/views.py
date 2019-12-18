from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.http import HttpResponseRedirect
from register.forms import UserLoginForm,LoginForm
from django.shortcuts import render_to_response
from django.http import *
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from ExpenseManagerProject import settings
# Create your views here.


def register(request):
    context ={}
    registered = False
    if request.POST:
        form = UserLoginForm(request.POST)
        breakpoint()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request,"The username is already taken")
            if len(username) > 10 :
                messages.error(request,"Username can contain atmost 10 characters")
            password = form.cleaned_data.get('password')
            repassword = form.cleaned_data.get('repassword')
            if password == repassword:
                user = form.save()
                user.set_password(user.password)
                user.save()
                registered = True
                return render(request,'index.html',{'registered':registered})
            else:
                messages.error(request,"Passwords don't match")
        else:
           messages.error(request,form.errors)
    else:
        form = UserLoginForm()

    context['form'] = form
    return render(request,'register.html',context)

def login_page(request):
    context = {}
    logged_in =  False
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            breakpoint()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    logged_in = True
                    return render(request,'base.html',{'logged_in':logged_in})
                    #return HttpResponseRedirect((reverse('index')))
                else:
                    messages.error(request, 'User is not active')
                    #return HttpResponse("User is not active")
            else:
                messages.error(request,'You don\'t have an account')
                #return HttpResponseRedirect(reverse('register'))
        else:
            messages.error(request, 'Invalid login details')
            #return HttpResponse("Invalid login details")
    else:
        form = LoginForm()

    context['form'] = form
    return render(request,'login.html',context)

@login_required()
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


