from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import IncomeForm, ExpenditureForm
from club.models import Club


def club_accounting(request, pk):
    club = Club.objects.get(pk=pk)
    income_form = IncomeForm(request.POST or None, prefix='income')
    expenditure_form = ExpenditureForm(request.POST or None, request.FILES or None, prefix='expd')
    if request.method == "POST":
        if income_form.is_valid():
            income = income_form.save(commit=False)
            income.accounting = club.accounting
            income.save()
        elif expenditure_form.is_valid():
            expenditure = expenditure_form.save(commit=False)
            expenditure.accounting = club.accounting
            expenditure.save()
        return redirect(reverse('finance:club_accounting', kwargs={'pk': pk, }))
    ctx = {
            'club': club,
            'income_all': club.accounting.income_set.all().order_by('income_at'),
            'expd_all': club.accounting.expenditure_set.all().order_by('expd_at'),
            'income_form': income_form,
            'expenditure_form': expenditure_form,
    }

    return render(request, 'finance/club_accounting.html', ctx)

