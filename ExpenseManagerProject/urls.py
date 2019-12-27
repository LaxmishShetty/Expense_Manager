"""ExpenseManagerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ExpenseManager import views as expense_manager_views
from register import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$',expense_manager_views.home,name='home'),
    url(r'^$',expense_manager_views.index,name='index'),
    url(r'^login$',views.login_page,name='login'),
    url(r'^register$',views.register,name='register'),
    url(r'^logout$',views.logout_page,name='logout'),
    url(r'^food$',expense_manager_views.food,name='food'),
    url(r'^petrol$',expense_manager_views.petrol,name='petrol'),
    url(r'clothes$',expense_manager_views.clothes,name='clothes'),
    url(r'^daywise$',expense_manager_views.daywise,name='daywise'),
    #url(r'^daywiseresults',expense_manager_views.daywiseresults,name='daywiseresults'),
]
