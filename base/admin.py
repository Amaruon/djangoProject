from django.contrib import admin

# Register your models here.

from .models import Expense, ExpenseItem

admin.site.register(ExpenseItem)
admin.site.register(Expense)
