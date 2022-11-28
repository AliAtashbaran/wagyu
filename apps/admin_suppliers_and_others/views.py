from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseForbidden
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView


from .forms import Employee_payroll_form
from .models import Employee_payroll_model


# -------------------------

def employee_payroll_working(employee):
    basic_daily=employee.basic//30
    # add to the salary:
    add_unclaimed_vac=employee.unclaimed_vacation_days*basic_daily
    # deduct from salary
    deduct_absense=employee.absense_days*basic_daily
    
    gross=(employee.basic+employee.up_sell+employee.allowance+employee.child_allowance+add_unclaimed_vac)
  
    deduct=employee.insurance_carried_employee+deduct_absense

    tax=(gross-deduct)*0.32
    net_salary=round(gross-(deduct+tax+employee.cash_in_hand))
    def payrol_db_update():
        employee.unclaimed_vacation=add_unclaimed_vac
        employee.deduction_absense=deduct_absense
        employee.deduction_tax=tax
        employee.net_salary=net_salary
        employee.save()
    payrol_db_update()

# ---------------------------


class Employe_payroll_view(View):

    def get(self,request,*args,**kwargs):
        if request.user.username in ['Ali0009']:
            form=Employee_payroll_form()
            return render(request,'employee/employee_payroll.html',{'form':form,})
        else:
            return HttpResponseForbidden('You have no access to this page.')

    def post(self,request,*args,**kwargs):
        form=Employee_payroll_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            employee_payroll=Employee_payroll_model.objects.get(employee=data['employee'])
            employee_payroll.up_sell=data['up_sell']
            employee_payroll.unclaimed_vacation_days=data['unclaimed_vacation_days']
            employee_payroll.absense_days=data['absense_days']
            employee_payroll.cash_in_hand=data['cash_in_hand']
            employee_payroll.save()

            employee_payroll_working(employee_payroll)
            
            return redirect('payroll',id=employee_payroll.id)
        else:
            return render(request,'employee/employee_payroll.html',{'form':form,})
# ----------------------------------

def show_employee_payroll_details(request,id):
    if request.user.username in {'Ali0009'}:
        employee=Employee_payroll_model.objects.get(id=id)
        context={'payroll':employee}
        return render(request,'Employee/emp_payroll_details.html',context) 
    else:
        return HttpResponseForbidden('Sorry you have no access to this page.')

# -----------------------------------


    



            

