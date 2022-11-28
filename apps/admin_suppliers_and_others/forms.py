from django import forms
from .models import Employee_payroll_model


class Employee_payroll_form(forms.ModelForm):

    up_sell=forms.IntegerField(initial=0,label='Product Up Sell',widget=forms.NumberInput(attrs={'class':'user_formControl'}))
    unclaimed_vacation_days=forms.IntegerField(initial=0,label='Unclaimed Vacation Days',widget=forms.NumberInput(attrs={'class':'user_formControl'}))
    absense_days=forms.IntegerField(initial=0,label='Absense Days',widget=forms.NumberInput(attrs={'class':'user_formControl'}))
    cash_in_hand=forms.IntegerField(initial=0,label='Cash In Hand',widget=forms.NumberInput(attrs={'class':'user_formControl'}))



    class Meta:
        model =Employee_payroll_model 
        fields = ('up_sell','unclaimed_vacation_days','absense_days','cash_in_hand','employee')

