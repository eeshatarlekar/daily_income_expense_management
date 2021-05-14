from django.shortcuts import render,HttpResponse,redirect
from .models import UserInfo,Income,Expense
from django.contrib.auth import login,logout,authenticate
from .forms import UserForm,IncomeForm,ExpenseForm,LoginForm

def home(request):
   bal=getbal(request)
   return render(request,'index.html')

def adduser(request):
   if request.method=='POST':
      f=UserForm(request.POST)
      f.save()
      return redirect('/')
   else:
      f=UserForm
      return render(request,'register.html',{'form':f})

def addIncome(request):
   if request.method=='POST':
      f=IncomeForm(request.POST)
      f.save()
      return redirect('/')
   else:
      f=IncomeForm
      return render(request,'forms.html',{'form':f})

def addExpense(request):
   if request.method=='POST':
      f=ExpenseForm(request.POST)
      f.save()
      return redirect('/')
   else:
      f=ExpenseForm
      return render(request,'forms.html',{'form':f})


def IncomeList(request):
   id=request.session.get('uid')
   f=Income.objects.filter(id=id)
   return render(request,'income_list.html',{'f':f})

def expenseList(request):
   id=request.session.get('uid')
   f=Expense.objects.filter(id=id)
   return render(request,'expense_list.html',{'f':f})


def login_view(request):
   if request.method=='POST':
      uname=request.POST.get('username')
      pword=request.POST.get('password')
      details=authenticate(request,username=uname,password=pword)
      
      if details is not None:
         request.session['uid']=details.id
         login(request, details)
         return redirect('/')
      else:
         return HttpResponse('Invalid username or password')
   else:
      f=LoginForm
      return render(request,'login.html',{'form':f})


def logout_view(request):
   logout(request)
   return redirect('/')
      
def deleteinc(request,id):
  
   del_id=Income.objects.get(id=id)
   del_id.delete()
   return redirect('/')

def deleteexp(request,id):
   del_id=Expense.objects.get(id=id)
   del_id.delete()
   return redirect('/')

def getbal(request):
   totalInc=0
   id=request.session.get('uid')
   inc=Income.objects.filter(id=id)

   for i in inc:
      totalInc+=i

   return(totalInc)


   









    