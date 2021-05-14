from django import forms
from .models import UserInfo,Income,Expense,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','age','contact','email','password1','password2']

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields='__all__'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model=login
        fields='__all__'
