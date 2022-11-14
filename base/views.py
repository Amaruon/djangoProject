from django.shortcuts import render
from .models import Expense

# Create your views here.

reps = [
    {'id': 1, 'name': 'Expenses by category'},
    {'id': 2, 'name': 'Expenses forecast'},
    {'id': 3, 'name': 'Profit n loss'},
]


def home(request):
    return render(request, 'home.html')


def report_page(request):
    context = {'reps': reps}
    return render(request, 'report-page.html', context)


def report(request, pk):
    rep = None
    for i in reps:
        if i['id'] == int(pk):
            rep = i
    context = {'report': rep}
    return render(request, 'report.html', context)


def expense(request):
    context = {'expenses': Expense.objects.all()}
    return render(request, 'expenses.html', context)
