from django.db import models
from django.contrib.auth.models import User


class UserInfo(User):
    age=models.IntegerField()
    contact=models.IntegerField()

    class Meta:
        db_table='user_info'

class Income(models.Model):
    income=models.IntegerField()
    incomeType=models.CharField(max_length=20)
    incomeDate=models.IntegerField()
    description=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Expense(models.Model):
    expense=models.IntegerField()
    expenseType=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)



