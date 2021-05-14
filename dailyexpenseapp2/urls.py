"""dailyexpenseproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views as v

urlpatterns = [
    path('adduser',v.adduser,name='adduser'),
    path('addincome',v.addIncome,name='addincome'),
    path('addexpense',v.addExpense,name='addExpense'),
    path('incomelist',v.IncomeList,name='incomeList'),
    path('expenseList',v.expenseList,name='expenseList'),
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name='logout'),
    path('dincome/<int:id>/',v.deleteinc,name='deleteinc'),
    path('dexpense/<int:id>/',v.deleteexp,name='deleteexp'),


  
  
]
