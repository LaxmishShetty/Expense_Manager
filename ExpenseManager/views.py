from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    context={'x':'hello world'}

    return render(request,'index.html')








