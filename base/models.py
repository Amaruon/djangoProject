from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExpenseItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_item = models.CharField(max_length=40)
    expense_description = models.TextField(max_length=250, null=True)


class Statements(models.Model):
    statement = models.CharField(max_length=40)


class AccountTypes(models.Model):
    account_type = models.CharField(max_length=40)


class DefaultChartOfAccounts(models.Model):
    account_number = models.CharField(max_length=8, primary_key=True)
    account_type = models.ForeignKey(AccountTypes, on_delete=models.CASCADE)
    account_statement = models.ForeignKey(Statements, on_delete=models.CASCADE)
    account_description = models.TextField(max_length=250, null=True)


class UserChartOfAccounts(DefaultChartOfAccounts):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    expense_item = models.ForeignKey(ExpenseItem, on_delete=models.CASCADE)
