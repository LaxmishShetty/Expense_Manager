from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from ExpenseManager.models import Category
from ExpenseManager.forms import FoodForm,PetrolForm,ClothesForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        logged_in = True
        user = request.user.username
        userr = User.objects.get(username=user)
        Expenses = Category.objects.get(user=userr).total_expense
        Petrol_expenses = Category.objects.get(user=userr).petrol_total_expense
        Clothes_expenses = Category.objects.get(user=userr).clothes_total_expense
        #return HttpResponseRedirect(reverse('index'))
        return render(request,'index.html',{'logged_in':logged_in,'Expenses':Expenses,'Petrol_expenses':Petrol_expenses,'Clothes_expenses':Clothes_expenses})
    else:
        return render(request,'login.html')



def home(request):
    if request.user.is_authenticated:
        logged_in = True
        return render(request,'index.html',{'logged_in':logged_in})
    else:
        return render(request,'homepage.html')


def food(request):
    if request.user.is_authenticated:
        user = request.user.username
        if request.method == "POST":
            form = FoodForm(request.POST)
            if form.is_valid():
                foodname = form.cleaned_data.get('Name')
                foodexpense = form.cleaned_data.get('Expense')
                foodDate = form.cleaned_data.get('Datee')
                userr = User.objects.get(username=user)
                previous_total_expense = Category.objects.get(user=userr)
                x = previous_total_expense.total_expense
                foodinfo = Category.objects.filter(user=userr).update(total_expense=foodexpense+x)
                Expenses = Category.objects.get(user=userr).total_expense
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request,form.errors)
        else:
            form = FoodForm()
    return render(request,'food.html')


def petrol(request):
    if request.user.is_authenticated:
        user = request.user.username
        if request.method == 'POST':
            form = PetrolForm(request.POST)
            breakpoint()
            if form.is_valid():
                petrol_expense = form.cleaned_data.get('Expense')
                petrol_date = form.cleaned_data.get('Datee')
                userr = User.objects.get(username=user)
                previous_petrol_total_expense = Category.objects.get(user=userr)
                x = previous_petrol_total_expense.petrol_total_expense
                Category.objects.filter(user=userr).update(petrol_total_expense=x + petrol_expense)
                Petrol_Expenses = Category.objects.get(user=userr).petrol_total_expense
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request,form.errors)
        else:
            form = PetrolForm()

    return render(request,'petrol.html')

def clothes(request):
    if request.user.is_authenticated:
        user = request.user.username
        if request.method == 'POST':
            form = ClothesForm(request.POST)
            if form.is_valid():
                clothes_type = form.cleaned_data.get('Cloth_Type')
                clothes_expense = form.cleaned_data.get('Expense')
                clothes_date = form.cleaned_data.get('Datee')
                userr = User.objects.get(username=user)
                previous_clothes_total_expense = Category.objects.get(user=userr)
                x = previous_clothes_total_expense.clothes_total_expense
                Category.objects.filter(user=userr).update(clothes_total_expense=x+clothes_expense)
                Clothes_expenses = Category.objects.get(user=userr).clothes_total_expense
                Category.objects.filter(user=userr).update(cloth_type=clothes_type)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request,form.errors)

        else:
            form = ClothesForm()

    return render(request,'clothes.html')







