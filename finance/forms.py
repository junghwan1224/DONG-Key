from django import forms
from .models import Income, Expenditure


class IncomeForm(forms.ModelForm):
    income_at = forms.DateField()

    class Meta:
        model = Income
        exclude = ('accounting', )
    prefix = 'income'


class ExpenditureForm(forms.ModelForm):
    expd_at = forms.DateField()

    class Meta:
        model = Expenditure
        exclude = ('accounting', )
    prefix = 'expd'