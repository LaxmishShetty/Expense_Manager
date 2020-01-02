from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from ExpenseManager.models import Category,Date
from ExpenseManager.forms import FoodForm,PetrolForm,ClothesForm,DaywiseForm
from django.contrib import messages
import datetime

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        logged_in = True
        user = request.user.username
        try:
            userr = User.objects.get(username=user)
            if Category.objects.get(user=userr).exists():
            #y = x.datefield
                Expenses = Category.objects.get(user=userr).total_expense
                Petrol_expenses = Category.objects.get(user=userr).petrol_total_expense
                Clothes_expenses = Category.objects.get(user=userr).clothes_total_expense
                Total_expenses = Expenses + Petrol_expenses + Clothes_expenses
            else:
                Category.objects.create(user=userr)
                Expenses = Category.objects.get(user=userr).total_expense
                Petrol_expenses = Category.objects.get(user=userr).petrol_total_expense
                Clothes_expenses = Category.objects.get(user=userr).clothes_total_expense
                Total_expenses = Expenses + Petrol_expenses + Clothes_expenses
            return render(request, 'index.html',
                          {'logged_in': logged_in, 'Expenses': Expenses, 'Petrol_expenses': Petrol_expenses,
                           'Clothes_expenses': Clothes_expenses,'Total_expenses':Total_expenses})

        except Category.DoesNotExist:
            user = None
        return render(request,'index.html',{'logged_in':logged_in})
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
                if Category.objects.filter(user=userr).exists():
                    if Date.objects.filter(dateField=foodDate).exists():
                        x = Date.objects.get(dateField=foodDate).food_expense
                        Date.objects.filter(dateField=foodDate).update(food_expense=foodexpense + x)
                    else:
                        Date.objects.create(dateField=foodDate)
                        x = Date.objects.get(dateField=foodDate).food_expense
                        Date.objects.filter(dateField=foodDate).update(food_expense=foodexpense + x)
                    previous_total_expense = Category.objects.get(user=userr)
                    x = previous_total_expense.total_expense
                    foodinfo = Category.objects.filter(user=userr).update(total_expense=foodexpense + x)
                    Category.objects.filter(user=userr).update(datefield=foodDate)
                    Category.objects.filter(user=userr).update(name=foodname)
                    Expenses = Category.objects.get(user=userr).total_expense
                    Total_expenses = previous_total_expense.total_expense + previous_total_expense.petrol_total_expense + previous_total_expense.clothes_total_expense
                    res = calculate_expenses_in_a_day(foodDate,foodexpense)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    cr = Category.objects.create(user=userr)
                    if Date.objects.filter(dateField=foodDate).exists():
                        x = Date.objects.get(dateField=foodDate).food_expense
                        Date.objects.filter(dateField=foodDate).update(food_expense=foodexpense + x)
                    else:
                        Date.objects.create(dateField=foodDate)
                        x = Date.objects.get(dateField=foodDate).food_expense
                        Date.objects.filter(dateField=foodDate).update(food_expense=foodexpense + x)
                    previous_total_expense = Category.objects.get(user=userr)
                    x = previous_total_expense.total_expense
                    foodinfo = Category.objects.filter(user=userr).update(total_expense=foodexpense+x)
                    Category.objects.filter(user=userr).update(name=foodname)
                    Expenses = Category.objects.get(user=userr).total_expense
                    Total_expenses = previous_total_expense.total_expense + previous_total_expense.petrol_total_expense + previous_total_expense.clothes_total_expense
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
            if form.is_valid():
                petrol_expense = form.cleaned_data.get('Expense')
                petrol_date = form.cleaned_data.get('Datee')
                userr = User.objects.get(username=user)
                if Category.objects.filter(user=userr).exists():
                    if Date.objects.filter(dateField=petrol_date).exists():
                        x = Date.objects.get(dateField=petrol_date).petrol_expense
                        Date.objects.filter(dateField=petrol_date).update(petrol_expense=petrol_expense + x)
                    else:
                        Date.objects.create(dateField=petrol_date)
                        x = Date.objects.get(dateField=petrol_date).petrol_expense
                        Date.objects.filter(dateField=petrol_date).update(petrol_expense=petrol_expense + x)
                    previous_petrol_total_expense = Category.objects.get(user=userr)
                    x = previous_petrol_total_expense.petrol_total_expense
                    Category.objects.filter(user=userr).update(petrol_total_expense=x + petrol_expense)
                    Petrol_Expenses = Category.objects.get(user=userr).petrol_total_expense
                    Total_expenses = previous_petrol_total_expense.total_expense + previous_petrol_total_expense.petrol_total_expense + previous_petrol_total_expense.clothes_total_expense
                    return HttpResponseRedirect(reverse('index'))
                else:
                    cr = Category.objects.create(user=userr)
                    if Date.objects.filter(dateField=petrol_date).exists():
                        x = Date.objects.get(dateField=petrol_date).petrol_expense
                        Date.objects.filter(dateField=petrol_date).update(petrol_expense=petrol_expense + x)
                    else:
                        Date.objects.create(dateField=petrol_date)
                        x = Date.objects.get(dateField=petrol_date).petrol_expense
                    previous_petrol_total_expense = Category.objects.get(user=userr)
                    x = previous_petrol_total_expense.petrol_total_expense
                    Category.objects.filter(user=userr).update(petrol_total_expense=x + petrol_expense)
                    Petrol_Expenses = Category.objects.get(user=userr).petrol_total_expense
                    Total_expenses = previous_petrol_total_expense.total_expense + previous_petrol_total_expense.petrol_total_expense + previous_petrol_total_expense.clothes_total_expense
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
                if Category.objects.filter(user=userr).exists():
                    if Date.objects.filter(dateField=clothes_date).exists():
                        x = Date.objects.get(dateField=clothes_date).cloth_expense
                        Date.objects.filter(dateField=clothes_date).update(cloth_expense=clothes_expense + x)
                    else:
                        Date.objects.create(dateField=clothes_date)
                        x = Date.objects.get(dateField=clothes_date).cloth_expense
                        Date.objects.filter(dateField=clothes_date).update(cloth_expense=clothes_expense + x)
                    previous_clothes_total_expense = Category.objects.get(user=userr)
                    x = previous_clothes_total_expense.clothes_total_expense
                    Category.objects.filter(user=userr).update(clothes_total_expense=x + clothes_expense)
                    Clothes_expenses = Category.objects.get(user=userr).clothes_total_expense
                    Category.objects.filter(user=userr).update(cloth_type=clothes_type)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    cr = Category.objects.create(user=userr)
                    if Date.objects.filter(dateField=clothes_date).exists():
                        x = Date.objects.get(dateField=clothes_date).cloth_expense
                        Date.objects.filter(dateField=clothes_date).update(cloth_expense=clothes_expense + x)
                    else:
                        Date.objects.create(dateField=clothes_date)
                        x = Date.objects.get(dateField=clothes_date).cloth_expense
                        Date.objects.filter(dateField=clothes_date).update(cloth_expense=clothes_expense + x)
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



def calculate_expenses_in_a_day(fooddate,foodexpense):

    pass

def daywise(request):
    if request.user.is_authenticated:
        user = request.user.username
        if request.method == 'POST':
            form = DaywiseForm(request.POST)
            if form.is_valid():
                entered_date = form.cleaned_data.get('DayWiseDate')
                if Date.objects.filter(dateField=entered_date).exists():
                    x = Date.objects.get(dateField=entered_date).food_expense
                    y = Date.objects.get(dateField=entered_date).petrol_expense
                    z = Date.objects.get(dateField=entered_date).cloth_expense
                    total = x + y + z
                    return render(request,'daywiseresults.html',{'date':entered_date,'foodexpense':x,'petrolexpense':y,'clothexpense':z,'totalexpenses':total})
                    #return HttpResponseRedirect(reverse('index'))
                else:
                    messages.error(request,"You don't have any expenses on this date")
            else:
                messages.error(request,form.errors)

        else:
            form = DaywiseForm()
    return render(request,'daywise.html')


# def daywiseresults(request):
#     if request.user.is_authenticated:
#         user = request.user.username
#         x = Date.objects.get(dateField=entered_date).food_expense
#         y = Date.objects.get(dateField=entered_date).petrol_expense
#         z = Date.objects.get(dateField=entered_date).cloth_expense





