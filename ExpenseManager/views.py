from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={'x':'hello world'}

    return render(request,'index.html',context)

def login(request):
    return HttpResponse("its login")


