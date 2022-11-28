from django.contrib import admin
from .models import*

@admin.register(Supplier_model)
class Supplier_arofile_admin(admin.ModelAdmin):
    exclude=('',)
    search_fields=('company','active')


# ---------------------------------
@admin.register(Employee_Model)
class Employee_profile_admin(admin.ModelAdmin):
    exclude=('',)
    search_fields=('lastname','employed')
# -------------------------------

@admin.register(Client_Profile_model)
class Client_profile_admin(admin.ModelAdmin):
    exclude=('',)
    search_fields=('lastname',)

# -------------------------------
@admin.register(Employee_payroll_model)
class Employee_payroll_admin(admin.ModelAdmin):
    exclude=('',)
    search_fields=('employee',)
    readonly_fields=('unclaimed_vacation_days','unclaimed_vacation','absense_days','deduction_absense','deduction_tax','net_salary')
# -------------------------------
