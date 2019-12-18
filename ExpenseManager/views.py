from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        logged_in = True
        return render(request,'index.html',{'logged_in':logged_in})
    else:
        return render(request,'login.html')



def home(request):
    return render(request,'base.html')




